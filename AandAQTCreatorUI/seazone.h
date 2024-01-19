#ifndef SEAZONE_H
#define SEAZONE_H

#include <QDialog>

namespace Ui {
class seazone;
}

class seazone : public QDialog
{
    Q_OBJECT

public:
    explicit seazone(QWidget *parent = nullptr);
    ~seazone();

private:
    Ui::seazone *ui;
};

#endif // SEAZONE_H
