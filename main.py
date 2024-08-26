from PyQt6.QtWidgets import *

from file_help import *

notes = read_from_file()
print(notes)
app = QApplication([])
window = QWidget()


text_edit = QTextEdit()


list_notes_lbl = QLabel("список заміток")
notes_list = QListWidget()
notes_list.addItems(notes)
create_note_btn = QPushButton("створити замітку")
delete_note_btn = QPushButton("видалити замітку")
save_note_btn = QPushButton("зберегти замітку")
list_teg_lbl = QLabel("список тегів")
tegs_list = QListWidget()
teg_input = QLineEdit()
add_teg_btn = QPushButton("додати до замітки")
delete_teg_btn = QPushButton("відкріпити від замітки")
search_note_btn = QPushButton("шукати замітки по тегу")


main_line = QHBoxLayout()
main_line.addWidget(text_edit)
v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
h1 = QHBoxLayout()
h1.addWidget(create_note_btn)
h1.addWidget(delete_note_btn)
v1.addLayout(h1)
v1.addWidget(save_note_btn)
v1.addWidget(list_teg_lbl)
v1.addWidget(tegs_list)
v1.addWidget(teg_input)
h2 = QHBoxLayout()
h2.addWidget(add_teg_btn)
h2.addWidget(delete_teg_btn)
v1.addLayout(h2)
v1.addWidget(search_note_btn)

main_line.addLayout(v1)


window.setLayout(main_line)

def show_note():
    key = notes_list.selectedItems()[0].text()
    text_edit.setText(notes[key]['текст'])
    tegs_list.clear()
    tegs_list.addItems(notes[key]['теги'])

def save_note():
    key = notes_list.selectedItems()[0].text()
    notes[key] = text_edit.toPlainText()
    write_in_file(notes)

save_note_btn.clicked.connect(save_note)
notes_list.itemClicked.connect(show_note)
window.show()
app.exec()
