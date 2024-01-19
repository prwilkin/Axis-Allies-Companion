#ifndef CHANGECOUNTRY_H
#define CHANGECOUNTRY_H

#include <QDialog>

namespace Ui {
class changeCountry;
}

class changeCountry : public QDialog
{
    Q_OBJECT

public:
    explicit changeCountry(QWidget *parent = nullptr);
    ~changeCountry();

private:
    Ui::changeCountry *ui;
};

#endif // CHANGECOUNTRY_H
