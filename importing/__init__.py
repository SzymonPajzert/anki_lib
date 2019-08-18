# -*- coding: utf-8 -*-
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki_lib.importing.csvfile import TextImporter
from anki_lib.importing.apkg import AnkiPackageImporter
from anki_lib.importing.anki2 import Anki2Importer
from anki_lib.importing.supermemo_xml import SupermemoXmlImporter
from anki_lib.importing.mnemo import MnemosyneImporter
from anki_lib.importing.pauker import PaukerImporter
from anki_lib.lang import _

Importers = (
    (_("Text separated by tabs or semicolons (*)"), TextImporter),
    (_("Packaged Anki Deck/Collection (*.apkg *.colpkg *.zip)"), AnkiPackageImporter),
    (_("Mnemosyne 2.0 Deck (*.db)"), MnemosyneImporter),
    (_("Supermemo XML export (*.xml)"), SupermemoXmlImporter),
    (_("Pauker 1.8 Lesson (*.pau.gz)"), PaukerImporter),
    )
