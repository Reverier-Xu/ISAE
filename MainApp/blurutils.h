#ifndef _BLURUTILS_H_

#define _BLURUTILS_H_

#include <QImage>

QImage blurred(const QImage& image, const QRect& rect, int radius, bool alphaOnly = false);

#endif
