#include "seazone.h"
#include "ui_seazone.h"

seazone::seazone(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::seazone)
{
    ui->setupUi(this);
}

seazone::~seazone()
{
    delete ui;
}
