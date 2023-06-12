# Homework 5

**周雨豪  2018013399  软件92**



## 1 贝叶斯决策

(1)
$$
\begin{align*}
&g_i(x)=-\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i)-\frac{d}{2}\ln(2\pi)-\frac{1}{2}\ln \left|\Sigma_i\right|+\ln p(\omega_i) \\
\\
&两类分类判别边界满足\ g_1(x)=g_2(x) \\

&g_1(x)-g_2(x)=(\mu_1^T\Sigma_1^{-1}-\mu_2^T\Sigma_2^{-1})x+(-\frac{1}{2}\mu_1^T\Sigma_1^{-1}\mu_1 + \frac{1}{2}\mu_2^T\Sigma_2^{-1}\mu_2) \\

&=(\left[\begin{array}{c}
1 & 2
\end{array}\right]
-
\left[\begin{array}{c}
3 & 1
\end{array}\right])x
+
\frac{1}{2}
(-
\left[\begin{array}{c}
1 & 2
\end{array}\right]
\left[\begin{array}{c}
1 \\ 2
\end{array}\right]
+
\left[\begin{array}{c}
3 & 1
\end{array}\right]
\left[\begin{array}{c}
3 \\ 1
\end{array}\right]
) \\
&=-2x_1+x_2+\frac{5}{2}
\\
&决策边界为 -2x_1+x_2+\frac{5}{2} = 0
\end{align*}
$$
(2) 决策边界会平移。

(3)
$$
\begin{align*}
&\Sigma_1^{-1}=
\left[\begin{array}{c}
1 & 0 \\
-1/2 & -1/2 \\
\end{array}\right] \\
\\
&g_1(x)-g_2(x)=(-\frac{1}{2}x^T\Sigma_1^{-1}x+\frac{1}{2}x^T\Sigma_2^{-1}x)
+(\mu_1^T\Sigma_1^{-1}-\mu_2^T\Sigma_2^{-1})x\\
&+(-\frac{1}{2}\mu_1^T\Sigma_1^{-1}\mu_1 + \frac{1}{2}\mu_2^T\Sigma_2^{-1}\mu_2-\frac{1}{2}\ln \left|\Sigma_1\right|+\frac{1}{2}\ln \left|\Sigma_2\right|) \\
&=\frac{1}{2}(-
\left[\begin{array}{c}
x_1 & x_2
\end{array}\right]
\left[\begin{array}{c}
1 & 0 \\
-1/2 & -1/2 \\
\end{array}\right]
\left[\begin{array}{c}
x_1 \\ x_2
\end{array}\right]
+
\left[\begin{array}{c}
x_1 & x_2
\end{array}\right]
I
\left[\begin{array}{c}
x_1 \\ x_2
\end{array}\right]
)\\
&+(
\left[\begin{array}{c}
0 & 0
\end{array}\right]
\left[\begin{array}{c}
1 & 0 \\
-1/2 & -1/2 \\
\end{array}\right]
-
\left[\begin{array}{c}
1 & 2
\end{array}\right]
\left[\begin{array}{c}
1 & 0 \\
0 & 1 \\
\end{array}\right]
)\left[\begin{array}{c}
x_1 \\ x_2
\end{array}\right] \\
&+\frac{1}{2}(-
\left[\begin{array}{c}
0 & 0
\end{array}\right]
\left[\begin{array}{c}
1 & 0 \\
-1/2 & -1/2 \\
\end{array}\right]
\left[\begin{array}{c}
0 \\ 0
\end{array}\right]
+
\left[\begin{array}{c}
1 & 2
\end{array}\right]
\left[\begin{array}{c}
1 & 0 \\
0 & 1 \\
\end{array}\right]
\left[\begin{array}{c}
1 \\ 2
\end{array}\right]
-
\ln\left|\begin{array}{c}
1 & 0 \\
1 & 2 \\
\end{array}\right|
+
\ln\left|\begin{array}{c}
1 & 0 \\
0 & 1 \\
\end{array}\right|
) \\
&=\frac{3}{4}x_2^2+\frac{1}{4}x_1x_2-x_1-2x_2+\frac{5}{2}\\
\\
&决策边界为\ \frac{3}{4}x_2^2+\frac{1}{4}x_1x_2-x_1-2x_2+\frac{5}{2}=0
\end{align*}
$$

<div style="page-break-after: always;"></div>

## 2 隐含马尔可夫模型

(1)
$$
\begin{align*}

\alpha_1=
&\left[\begin{array}{c}
0.2 \\ 0.4 \\ 0.4
\end{array}\right]
*
\left[\begin{array}{c}
0.5 \\ 0.4 \\ 0.3
\end{array}\right]
=
\left[\begin{array}{c}
0.1 \\ 0.16 \\ 0.12
\end{array}\right] \\
\\
&\left[\begin{array}{c}
0.1 \\ 0.16 \\ 0.12
\end{array}\right]
*
\left[\begin{array}{c}
0.5&0.2&0.3\\0.3&0.5&0.2\\0.2&0.3&0.5
\end{array}\right]
=
\left[\begin{array}{c}
0.05&0.02&0.03\\0.048&0.08&0.032\\0.024&0.036&0.06
\end{array}\right] \\

\alpha_2=
&\left[\begin{array}{c}
0.122 \\ 0.136 \\ 0.122
\end{array}\right]
*
\left[\begin{array}{c}
0.5 \\ 0.6 \\ 0.7
\end{array}\right]
=
\left[\begin{array}{c}
0.061 \\ 0.0816 \\ 0.0854
\end{array}\right] \\
\\
&\left[\begin{array}{c}
0.061 \\ 0.0816 \\ 0.0854
\end{array}\right]
*
\left[\begin{array}{c}
0.5&0.2&0.3\\0.3&0.5&0.2\\0.2&0.3&0.5
\end{array}\right]
=
\left[\begin{array}{c}
0.0305&0.0122&0.0183\\0.02448&0.0408&0.01632\\0.01708&0.02562&0.0427
\end{array}\right] \\

\alpha_3=
&\left[\begin{array}{c}
0.07206 \\ 0.07862 \\ 0.07732
\end{array}\right]
*
\left[\begin{array}{c}
0.5 \\ 0.4 \\ 0.3
\end{array}\right]
=
\left[\begin{array}{c}
0.03603 \\ 0.031448 \\ 0.023196
\end{array}\right]\\
\\
P(O|\lambda)&=0.03603+0.031448+0.023196=0.090674
\end{align*}
$$
(2)
$$
\begin{align*}

\delta_1 = 
&\left[\begin{array}{c}
0.2 \\ 0.4 \\ 0.4
\end{array}\right]
*
\left[\begin{array}{c}
0.5 \\ 0.4 \\ 0.3
\end{array}\right]
=
\left[\begin{array}{c}
0.1 \\ 0.16 \\ 0.12
\end{array}\right]
,\ \phi_1=\left[\begin{array}{c}
0 \\ 0 \\ 0
\end{array}\right] \\
\\

&\left[\begin{array}{c}
0.1 \\ 0.16 \\ 0.12
\end{array}\right]
*
\left[\begin{array}{c}
0.5&0.2&0.3\\0.3&0.5&0.2\\0.2&0.3&0.5
\end{array}\right]
=
\left[\begin{array}{c}
0.05&0.02&0.03\\0.048&0.08&0.032\\0.024&0.036&0.06
\end{array}\right] \\
\delta_2 = 
&\left[\begin{array}{c}
0.05 \\ 0.08 \\ 0.06
\end{array}\right]
*
\left[\begin{array}{c}
0.5 \\ 0.6 \\ 0.7
\end{array}\right]
=
*
\left[\begin{array}{c}
0.025 \\ 0.048 \\ 0.042
\end{array}\right]
,\ \phi_2=
\left[\begin{array}{c}
1 \\ 2 \\ 3
\end{array}\right] \\
\\

&\left[\begin{array}{c}
0.025 \\ 0.048 \\ 0.042
\end{array}\right]
*
\left[\begin{array}{c}
0.5&0.2&0.3\\0.3&0.5&0.2\\0.2&0.3&0.5
\end{array}\right]
=
\left[\begin{array}{c}
0.0125&0.005&0.0075\\
0.0144&0.024&0.0096\\
0.0084&0.0126&0.021
\end{array}\right]
\\

\delta_3=
&\left[\begin{array}{c}
0.0144 \\ 0.024 \\ 0.021
\end{array}\right]
*
\left[\begin{array}{c}
0.5 \\ 0.4 \\ 0.3
\end{array}\right]=
\left[\begin{array}{c}
0.0072 \\ 0.0096 \\ 0.0063
\end{array}\right]
,\ \phi_3=
\left[\begin{array}{c}
2 \\ 2 \\ 3
\end{array}\right] \\
\\
q_3=&S_2 ,
\ q_2=S_2,
\ q_1 =S_2,
\ 最可能的隐含序列状态为\ (S_2S_2S_2)
\end{align*}
$$