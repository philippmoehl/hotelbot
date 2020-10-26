from rasa.nlu.components import Component
from rasa.nlu.training_data import Message
import typing
from typing import Any, Optional, Text, Dict

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata

from spellchecker import SpellChecker

class SpellCheckerDE(Component):

    defaults = {}
    language_list = ["de"]

    def __init__(self, component_config=None):
        super(SpellCheckerDE, self).__init__(component_config)

    def process(self, message, **kwargs):
        mt =  message.text
        str = mt.translate(mt.maketrans('', '', '!\"#$%&\'()*+,.:;<=>?@[\]^_`{|}~'))
        words = str.split(' ')
        words = [word for word in words if word]
        spell = SpellChecker(language=None)
        spell.word_frequency.load_dictionary('resources/de.json.gz')
        spell.word_frequency.load_text_file('resources/hotel_lex.txt')
        
        for word in words:
            if word not in spell:
                mt = mt.replace(word, spell.correction(word))

        message.text = mt

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any
    ) -> "Component":
        if cached_component:
            return cached_component
        else:
            return cls(meta)
