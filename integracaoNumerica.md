<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

## Integração Numérica   

**Definição de Integral:** Seja uma **f** função contínua em um intervalo fechado **[a,b]** e tal que que f(x) $$\geqslant$$ 0, para todo **x $$\in$$ [a,b]**, logo a integral é dada como a área da região compreendida entre o eixo das abcissas e o curva da função f, para um x variando no intervalo fechado **[a,b]**. A área é dado por:

$$\int_{a}^{b} f(x) dx = \lim_{n\to\infty}\sum_{n=1}^{\infty}f(x)\Delta x, \Delta x = \dfrac{(b-a)}{n}$$

Em situações que a determinação da primitiva da função f(x) é complexa costuma-se utilizar métodos numéricos de integração que consistem em determinar a $$\int_{a}^{b} f(x) dx \simeq \int_{a}^{b} \phi (x) dx$$. Onde $$\phi (x)$$ pode ser tomado como uma função aproximadora de $$f(x)$$. Normalmente a função aproximadora toma forma de um polinômio devido a facilidade na determinação da integral desse tipo de função.

Logo a integração numérica pode ser dada através do seguinte somatório:

$$\sum_{n=1}^{\infty}\phi (x_i).\omega _i$$

<p align=”Justify”>Definição de Integral </p>

