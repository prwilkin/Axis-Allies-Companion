#include "bonus.h"
#include "ui_bonus.h"

Bonus::Bonus(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Bonus)
{
    ui->setupUi(this);
}

Bonus::~Bonus()
{
    delete ui;
}
