# Homework 3

**周雨豪  2018013399 软件92**



(1)
$$
\begin{align*}
&z=W_{Layer1}x =
\left[
\begin{matrix}
1.0 & 2.0 \\
0.5 & 1.2 \\
-0.5 & 1.0
\end{matrix}
\right]
\left[
\begin{matrix}
0.2\\0.5
\end{matrix}
\right]
=
\left[
\begin{matrix}
1.2\\0.7\\0.4
\end{matrix}
\right] \\
\\
&a=\sigma(z)=
\left[
\begin{matrix}
0.7685\\0.6682\\0.5987
\end{matrix}
\right] \\
&output = W_{Layer2}a =
\left[
\begin{matrix}
-0.5 & 1.0 & 0.5 \\
1.0 & -0.5 & 0.2
\end{matrix}
\right]
\left[
\begin{matrix}
0.7685\\0.6682\\0.5987
\end{matrix}
\right] =
\left[
\begin{matrix}
0.5833 \\ 0.5542
\end{matrix}
\right] \\
& Loss=0.6787
\end{align*}
$$


(2)
$$
\begin{align*}
&W_{Layer1}=
\left[
\begin{matrix}
0.9974 & 1.9934 \\
0.5033 & 1.2082 \\
-0.4993 & 1.0018
\end{matrix}
\right] \\
\\
&W_{Layer2}=
\left[
\begin{matrix}
-0.4621 & 1.0329 & 0.5295 \\
0.9621 & -0.5329 & 0.1705
\end{matrix}
\right] \\
\end{align*}
$$
