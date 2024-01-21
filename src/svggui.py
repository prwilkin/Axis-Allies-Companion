import sys

from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene


class SvgInteractiveViewer(QGraphicsView):
    def __init__(self, svgFilePath):
        super().__init__()

        # Load the SVG file
        self.svgItem = QGraphicsSvgItem(svgFilePath)
        self.setScene(QGraphicsScene(self))
        self.scene().addItem(self.svgItem)

    def mousePressEvent(self, event):
        # Find the item at the clicked position
        item = self.itemAt(event.pos())
        if item and isinstance(item, QGraphicsSvgItem):
            # Get the ID of the clicked element
            element_id = item.elementId()

            # Here you can add logic to map this element ID to its group ID
            group_id = self.find_group_id(element_id)

            # Now you can pass this group_id to your other functions
            print(f"Clicked on item with element ID: {element_id}, which belongs to group ID: {group_id}")

            # For example: #TODO
            # change_group_color('your_file.svg', group_id, '#FF0000')

    def find_group_id(self, element_id): # TODO
        # Logic to find the group ID based on element ID
        # This would be specific to your SVG structure
        # For now, it's just a placeholder function
        return "group_id_based_on_" + element_id


if __name__ == "__main__":
    app = QApplication(sys.argv)

    viewer = SvgInteractiveViewer("./Board/Board.svg")
    viewer.show()

    sys.exit(app.exec_())
