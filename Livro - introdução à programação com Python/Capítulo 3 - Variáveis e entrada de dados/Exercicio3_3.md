## Exercício 3.2: Complete a tabela a seguir utilizando _a = True_, _b = False_ e _c = True_ ##

### tabela:
| **Expressão** |     **Resultado**      |
|:-------------:|:----------------------:|
|    a and a    | **True** or **False**  |
|    b and b    | **True** or **False**  |
|     not c     | **True** or **False**  |
|     not b     | **True** or **False**  |
|     not a     | **True** or **False**  |
|    a and b    | **True** or **False**  |
|    b and c    | **True** or **False**  |
|    a or c     | **True** or **False**  |
|    b or c     | **True** or **False**  |
|    c or a     | **True** or **False**  |
|    c or b     | **True** or **False**  |
|    c or c     | **True** or **False**  |
|    b or b     | **True** or **False**  |

<br>

#### Exemplificando com números binários: ####
| a | b | c | a and a | b and b | not a | not b | not c | a and b | b and c | a or c | b or c | c or a | c or b | c or c | b or b |
|:-:|:-:|:-:|:-------:|:-------:|:-----:|:-----:|:-----:|:-------:|:-------:|:------:|:------:|:------:|:------:|:------:|:------:|
| 1 | 1 | 1 |    1    |    1    |   0   |   0   |   0   |    1    |    1    |   1    |   1    |   1    |   1    |   1    |   1    |
| 1 | 1 | 0 |    1    |    1    |   0   |   0   |   1   |    1    |    0    |   1    |   1    |   1    |   1    |   0    |   1    |
| 1 | 0 | 1 |    1    |    0    |   0   |   1   |   0   |    0    |    0    |   1    |   1    |   1    |   1    |   1    |   0    |
| 1 | 0 | 0 |    1    |    0    |   0   |   1   |   1   |    0    |    0    |   1    |   0    |   1    |   0    |   0    |   0    |
| 0 | 1 | 1 |    0    |    1    |   1   |   0   |   0   |    0    |    1    |   1    |   1    |   1    |   1    |   1    |   1    |
| 0 | 1 | 0 |    0    |    1    |   1   |   0   |   1   |    0    |    0    |   0    |   1    |   0    |   1    |   0    |   1    |
| 0 | 0 | 1 |    0    |    0    |   1   |   1   |   0   |    0    |    0    |   1    |   1    |   1    |   1    |   1    |   0    |
| 0 | 0 | 0 |    0    |    0    |   1   |   1   |   1   |    0    |    0    |   0    |   0    |   0    |   0    |   0    |   0    |

<br>

### Resposta:
| **Expressão** | **Resultado** |
|:-------------:|:-------------:|
|    a and a    |   **True**    |
|    b and b    |   **False**   |
|     not c     |   **False**   |
|     not b     |   **True**    |
|     not a     |   **False**   |
|    a and b    |   **False**   |
|    b and c    |   **False**   |
|    a or c     |   **True**    |
|    b or c     |   **True**    |
|    c or a     |   **True**    |
|    c or b     |   **True**    |
|    c or c     |   **True**    |
|    b or b     |   **False**   |