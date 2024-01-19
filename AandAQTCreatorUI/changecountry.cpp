#include "changecountry.h"
#include "ui_changecountry.h"

changeCountry::changeCountry(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::changeCountry)
{
    ui->setupUi(this);
}

changeCountry::~changeCountry()
{
    delete ui;
}
