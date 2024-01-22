import sys

from PyQt6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt


class SvgInteractiveViewer(QGraphicsView):
    def __init__(self, svgFilePath):
        super().__init__()
        # Load the SVG file using QSvgWidget
        self.svgWidget = QSvgWidget(svgFilePath)
        if not self.svgWidget.renderer().isValid():
            print(f"Failed to load SVG file: {svgFilePath}")
            return

        # Set the size of the SVG widget
        self.svgWidget.setFixedSize(781, 421)

        # Create a QGraphicsScene
        self.setScene(QGraphicsScene(self))

        # Add the SVG widget to the scene using a proxy widget
        self.proxyWidget = self.scene().addWidget(self.svgWidget)

        # Adjust the scene's size to fit the SVG widget
        self.scene().setSceneRect(0, 0, 789, 421)

        # Hide scrollbars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Optionally, fit the SVG in the view
        self.fitInView(self.proxyWidget, Qt.AspectRatioMode.KeepAspectRatio)
        # Enable mouse wheel zooming
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

        # Zoom level variables
        self.currentZoom = 1
        self.maxZoom = 5.0  # Maximum zoom level
        self.minZoom = 1  # Minimum zoom level

        self.elementCoords = self.parse_svg(svgFilePath)

    def parse_svg(self, svgFilePath):
        # Define the namespace for SVG
        namespace = {'svg': 'http://www.w3.org/2000/svg'}
        ET.register_namespace('', "http://www.w3.org/2000/svg")

        tree = ET.parse(svgFilePath)
        root = tree.getroot()

        elementCoords = {}
        # Iterate over all elements with an ID
        for element in root.findall('.//*[@id]', namespaces=namespace):
            id = element.get('id')
            # Attempt to extract x, y coordinates and width, height
            x = float(element.get('x', 0))
            y = float(element.get('y', 0))
            width = float(element.get('width', 0))
            height = float(element.get('height', 0))
            elementCoords[id] = (x, y, width, height)

        return elementCoords

    def mousePressEvent(self, event):
        scenePos = self.mapToScene(event.pos())
        clickedElement = None

        # Check if the click is within the bounds of any element
        for id, (x, y, width, height) in self.elementCoords.items():
            if x <= scenePos.x() <= x + width and y <= scenePos.y() <= y + height:
                clickedElement = id
                break

        if clickedElement:
            print(f"Clicked on element with ID: {clickedElement}")
            # Implement additional logic as needed

    def wheelEvent(self, event):
        factor = 1.2
        newZoom = self.currentZoom * (factor if event.angleDelta().y() > 0 else 1 / factor)

        if self.minZoom <= newZoom <= self.maxZoom:
            self.scale(factor if event.angleDelta().y() > 0 else 1 / factor,
                       factor if event.angleDelta().y() > 0 else 1 / factor)
            self.currentZoom = newZoom

    # def mousePressEvent(self, event):
    #     # Find the item at the clicked position
    #     item = self.itemAt(event.pos())
    #     if item and isinstance(item, QGraphicsSvgItem):
    #         # Get the ID of the clicked element
    #         element_id = item.elementId()
    #
    #         # Here you can add logic to map this element ID to its group ID
    #         group_id = self.find_group_id(element_id)
    #
    #         # Now you can pass this group_id to your other functions
    #         print(f"Clicked on item with element ID: {element_id}, which belongs to group ID: {group_id}")
    #
    #         # For example: # TODO
    #         # change_group_color('your_file.svg', group_id, '#FF0000')

    def find_group_id(self, element_id): # TODO
        # Logic to find the group ID based on element ID
        # This would be specific to your SVG structure
        # For now, it's just a placeholder function
        return "group_id_based_on_" + element_id


if __name__ == "__main__":
    app = QApplication(sys.argv)

    viewer = SvgInteractiveViewer("./board/board.svg")
    # viewer = SvgInteractiveViewer("./board/test.svg")
    viewer.show()

    sys.exit(app.exec_())
