Tipos de relacionamentos entre tabelas de um banco de dados.

1:1     -> Relacionamento Um para Um
1:N     -> Relacionamento Um para Muitos
N:N     -> Relacionamento Muitos para Muitos

Modelar um sistema de blog. Quais as regras que teremos que implementar nesse sistema?

1) As oistagens serão feitas por usuários. Cada usuário terá apenas 1 perfil dentro do sistema, e cada perfil pode ter
apenas um perfil associado
    - Usuario, PerfilDeUsuario

2) Cada usuário pode fazer quantas postagens quiser(0, 1 ou muitas), porém cada postegem terá como auto apenas 1 usuário
Nesse caso teremos uma relação de 1:N, entre usuários e postagens
    -Usuario, Postagem

3) Quando um usuário faz uma postagem, ele pode associar categorias(hastag) nessa postagem. Uma postagem pode ter diversas categorias, e uma categoria pode aparecer em diversas postagem. Isso caracteriza uma relação de N:N ( muitos para muitos)