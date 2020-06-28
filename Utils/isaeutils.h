/*
一些工具函数

0. 图片模糊算法
*/

#ifndef _ISAEUTILS_H_
#define _ISAEUTILS_H_

#include <QImage>

// 图片模糊算法
QImage blurred(const QImage& image, const QRect& rect, int radius,
               bool alphaOnly = false);

#endif
