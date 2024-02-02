#ifndef BONUS_H
#define BONUS_H

#include <QDialog>

namespace Ui {
class Bonus;
}

class Bonus : public QDialog
{
    Q_OBJECT

public:
    explicit Bonus(QWidget *parent = nullptr);
    ~Bonus();

private:
    Ui::Bonus *ui;
};

#endif // BONUS_H
