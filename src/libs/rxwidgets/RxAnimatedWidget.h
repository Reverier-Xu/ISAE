//
// Created by reverier on 2020/7/20.
//

#ifndef ISAE_RXANIMATEDWIDGET_H
#define ISAE_RXANIMATEDWIDGET_H

#include <QWidget>
#include <QPropertyAnimation>

class RxAnimatedWidget : public QWidget {
Q_OBJECT
    Q_PROPERTY(qreal currentAnimateValue READ currentAnimateValue WRITE setCurrentAnimateValue)
    Q_PROPERTY(qreal foldValue READ foldValue WRITE setFoldValue)
    Q_PROPERTY(qreal unfoldValue READ unfoldValue WRITE setUnfoldValue)
    Q_PROPERTY(bool isFolded READ isFolded WRITE setFolded)
    Q_PROPERTY(bool isVertical READ isVertical WRITE setVertical)

signals:
    void animationEnded();

public:
    explicit RxAnimatedWidget(QWidget *parent = nullptr);

    ~RxAnimatedWidget() override = default;

    void setFoldValue(qreal val) { this->m_foldValue = val; };

    void setUnfoldValue(qreal val) { this->m_unfoldValue = val; };

    void setCurrentAnimateValue(qreal val);

    void setVertical(bool val) { this->m_isVertical = val; }

    [[nodiscard]] bool isVertical() const { return this->m_isVertical; };

    [[nodiscard]] qreal currentAnimateValue() const { return this->m_currentAnimateValue; };

    [[nodiscard]] qreal foldValue() const { return this->m_foldValue; };

    [[nodiscard]] qreal unfoldValue() const { return this->m_unfoldValue; };

    [[nodiscard]] bool isFolded() const {
        return this->m_isFolded;
    }

    void setFolded(bool val) { this->m_isFolded = val; }

public slots:

    void doFold();

protected:
    qreal m_currentAnimateValue {};
    qreal m_foldValue {};
    qreal m_unfoldValue {};
    bool m_isFolded {};
    QPropertyAnimation m_animation;
    bool m_isVertical {};
};

#endif //ISAE_RXANIMATEDWIDGET_H
