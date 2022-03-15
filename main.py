import utf_imaging.ui
import utf_imaging.processing


def start_program():
    root = utf_imaging.ui.ImageUi(400, 600)
    root.configure(background="gray")

    root.mainloop()


if __name__ == "__main__":
    start_program()