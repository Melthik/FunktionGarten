Title: Complex Numbers
Category: Whittaker-Watson
Date: 2022-07-27 12:00
**Problem 2:**  Show that 1+4i, 2+7i, 3+10i, are collinear.

**Solution:** Consider the line passing through 1+4i and 2+7i defined by the equation z = a + (3a+1)i, where a $\in\mathbb{R}$. Inputting a=3 shows that 3+10i lies on this line and hence the three points are collinear.

**Problem 3:**  Show that a parabola can be drawn to pass through the representative points of the complex numbers 2+i, 4+4i, 6+9i, 8+16i, 10+25i.

**Solution:** Consider the parabola defined by the three points 2+i, 4+4i, 6+9i which will be of the form z = x + (ax$^2$ + bx +c)i, x, a, b, c $\in\mathbb{R}$. We have the equations
$$ 4a+2b+c = 1,
16a + 4b +c = 4,
36a + 6b + c = 9
$$
Solving these equations, we find the parameters defining the parabola passing through the three points are $a = \frac{1}{4}, b = 0, c= 0$. Thus, the parabola of interest is of the form z = x + ($\frac{1}{4}$x$^2$)i. It is then clear that the points 8 + 16i and 10 + 25i fall on this curve as well, corresponding to the points on the curve where x = 8 and 10.

**Problem 4:**  Determine the $n$th roots of unity by aid of the Argand diagram ; and show that the number of primitive roots is the number of integers less than n and prime to it. Prove that if $\theta_1$, $\theta_2$, $\theta_3$, ... be the arguments of the primitive roots, $\sum cos\,p\theta$ = 0 when p is a positive integer less than $\frac{n}{abc..k}$, where a,b,c,...k are the different constituent primes of n ; and that, when p = $\frac{n}{abc...k}$, $\sum cos\,p\theta$ = $\frac{(-1)^\mu n}{abc...k}$, where $\mu$ is the number of constituent primes.

**Solution:**  The roots of unit can be expressed by $z^n = 1$ which can be rewritten as $z = (cos (0+2\pi k)+ i sin(0+2\pi k))^\frac{1}{n}$. This can be further simplified to the expression $z = cos(\frac{2\pi k}{n}) + i sin(\frac{2\pi k}{n})$ for k $\in$ 0 2, ... n-1. This gives us the n desired roots of unity. It is evident that a root is a primitive root if and only if it may generate the root $z = cos(\frac{2\pi }{n}) + i sin(\frac{2\pi }{n})$. Rephrasing this condition, a root is primitive if and only if $ka \equiv 1\,mod\,n$ for some a $\in \mathbb{Z}$. 

By Bézout's identity, k relatively prime to n will satisfy this condition, while those not relatively prime will not. The number of primitive roots of unity is thus equivalent to the number of relatively prime integers less than n. 


