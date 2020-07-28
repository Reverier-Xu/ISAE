//
// Created by reverier on 2020/7/20.
//

#include "RxAnimatedWidget.h"

void RxAnimatedWidget::doFold() {
    if (isFolded() && this->m_animation.state() == QPropertyAnimation::Stopped) {
        this->m_animation.setStartValue(foldValue());
        this->m_animation.setEndValue(unfoldValue());
        this->m_animation.start();
        this->setFolded(false);
        emit this->animationEnded();
    } else if (this->m_animation.state() == QPropertyAnimation::Stopped) {
        this->m_animation.setStartValue(unfoldValue());
        this->m_animation.setEndValue(foldValue());
        this->m_animation.start();
        this->setFolded(true);
        emit this->animationEnded();
    }
}

void RxAnimatedWidget::setCurrentAnimateValue(qreal val) {
    this->m_currentAnimateValue = val;
    if (this->isVertical())
        this->setFixedHeight(val);
    else this->setFixedWidth(val);
}

RxAnimatedWidget::RxAnimatedWidget(QWidget *parent) : QWidget(parent) {
    this->setAttribute(Qt::WA_StyledBackground, true);
    this->m_animation.setTargetObject(this);
    this->m_animation.setPropertyName("currentAnimateValue");
    this->m_animation.setDuration(500);
    this->m_animation.setEasingCurve(QEasingCurve::InOutCubic);
    this->setFolded(false);
}
