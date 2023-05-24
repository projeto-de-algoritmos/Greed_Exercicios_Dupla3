# Explicação do problema

Uma escola tem N crianças. Cada criança tem talentos vocacionais em exatamente uma das seguintes áreas: programação, matemática ou educação física. 
A escola está organizando uma olimpíada. Ela será disputada por equipes. Cada equipe é formada por 3 alunos: o primeiro tem talentos em programação, o segundo em matemática e o terceiro em educação física. Além disso, um aluno só pode participar de exatamente uma equipe.

Qual é o número máximo de equipes que podem ser formadas?
OBS: o codeforces pede, além do número acima, formações possíveis de cada equipe.

## Dados e regras do problema

* Cada criança tem exatamente um talento
* Cada criança pode participar de exatamente uma equipe
* Nem todas as crianças vão participar da gincana
* Existem várias soluções possíveis. No entanto, queremos _o número máximo de equipes_, e não _todas as equipes possíveis_.

## Explicação da solução

A propriedade de escolha gulosa que escolhemos é: para uma criança C1, cujo talento é programação, agrupe-a com a primeira criança C2 (cujo talento é matemática) e a primeira criança C3 (cujo talento é educação física) que aparecer. 

Para tanto, vamos ter uma lista de crianças para cada categoria de talentos. Vamos iterar nas 3 listas e agrupar as 3 primeiras crianças que aparecerem em cada lista. Para cada equipe nova, vamos adicionar 1 ao número máximo de equipes. A iteração termina quando todas as crianças da categoria com o menor número de crianças forem alocadas numa equipe.
