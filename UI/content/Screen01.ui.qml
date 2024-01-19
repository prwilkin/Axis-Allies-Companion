/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.5
import QtQuick.Controls 6.5
import UntitledProject1
import QtQuick.Layouts
import FlowView
import QtQuick.Studio.Components
import QtQuick.Window

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Button {
        id: button
        text: qsTr("Next Phase")
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: -403
        anchors.horizontalCenterOffset: 528
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter

        Connections {
            target: button
            onClicked: animation.start()
        }
    }


    GroupItem {
        id: headerIPC
        x: 8
        y: 8

        Row {
            id: countries_icons
            x: 0
            y: 0
            width: 999
            height: 99
            padding: 0
            topPadding: 0

            Image {
                id: ussr
                width: 100
                height: 100
                source: "../../icons/ussr.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: ukeur
                width: 100
                height: 100
                source: "../../icons/ukeur.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: ukpac
                width: 100
                height: 100
                source: "../../icons/ukpac.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: anzac
                width: 100
                height: 100
                source: "../../icons/anzac.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: usa
                width: 100
                height: 100
                source: "../../icons/usa.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: china
                width: 100
                height: 100
                source: "../../icons/china.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: france
                width: 100
                height: 100
                source: "../../icons/france.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: germany
                width: 100
                height: 100
                source: "../../icons/germany.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: japan
                width: 100
                height: 100
                source: "../../icons/japan.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: italy
                width: 100
                height: 100
                source: "../../icons/italy.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        RowLayout {
            id: ipc_display
            x: 28
            y: 0
            width: 999
            height: 99

            ColumnLayout {
                id: ussrIPC
                width: 100
                height: 100

                Text {
                    id: ussrTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: ussrBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: ukeurIPC
                width: 100
                height: 100
                Text {
                    id: ukeurTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: ukeurBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: ukpacIPC
                width: 100
                height: 100
                Text {
                    id: ukpacTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: ukpacBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: anzacIPC
                width: 100
                height: 100
                Text {
                    id: anzacTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: anzacBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: usaIPC
                width: 100
                height: 100
                Text {
                    id: usaTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: usaBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: chinaIPC
                width: 100
                height: 100
                Text {
                    id: chinaTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: chinaBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: franceIPC
                width: 100
                height: 100
                Text {
                    id: franceTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: franceBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: germanyIPC
                width: 100
                height: 100
                Text {
                    id: germanyTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: germanyBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: japanIPC
                width: 100
                height: 100
                Text {
                    id: japanTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: japanBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }

            ColumnLayout {
                id: italyIPC
                width: 100
                height: 100
                Text {
                    id: italyTurn
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }

                Text {
                    id: italyBank
                    color: "#ffffff"
                    text: qsTr("Text")
                    font.pixelSize: 20
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font.hintingPreference: Font.PreferDefaultHinting
                    style: Text.Outline
                    font.bold: true
                }
            }
        }
    }

    RectangleItem {
        id: rectangle1
        x: 38
        y: 147
        width: 1027
        height: 277
        adjustBorderRadius: true
    }

    Text {
        id: text1
        x: 1151
        y: 24
        text: qsTr("Text")
        font.pixelSize: 20
    }
    states: [
        State {
            name: "clicked"
            when: button.checked
        }
    ]
}
