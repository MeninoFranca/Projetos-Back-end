
<body>
    <div class="container">
        <h1>Sequelize Model Generator</h1>
        <p>Este projeto tem como objetivo automatizar a geração de modelos Sequelize com base nas tabelas de um banco de dados MySQL (ou outros bancos suportados). O sistema conecta-se ao banco de dados, introspecta as tabelas e suas colunas, e utiliza um template Jinja2 para gerar automaticamente arquivos <code>.js</code> que representam os modelos Sequelize, prontos para serem utilizados em um projeto Node.js.</p>
        <h2>Objetivo 🎯</h2>
        <p>O principal objetivo deste projeto é facilitar o processo de criação de modelos Sequelize, evitando a necessidade de codificar manualmente cada modelo para cada tabela no banco de dados. A automação permite economizar tempo e reduzir a possibilidade de erros durante a criação dos modelos.</p>
        <h2>Estrutura do Projeto</h2>
        <pre><code>
/Geraçao_siquelize
│
├── /models                     Diretório onde os modelos Sequelize gerados serão armazenados
│
├── /templates                  Diretório onde se encontra o template Jinja2 para os arquivos .js
│   └── model_template.js       Template para geração de código dos modelos
│
├── main.py                     Script principal que executa a geração dos modelos
│
└── /config                     Configurações relacionadas ao banco de dados
    └── database.py             Script que contém a lógica de introspecção do banco de dados
        </code></pre>
        <h2>Como Funciona ⚙️</h2>
        <ol>
            <li><strong>Introspecção do Banco de Dados</strong>: O projeto utiliza SQLAlchemy para se conectar ao banco de dados e refletir as tabelas e colunas, extraindo informações essenciais como tipos de dados, chaves primárias, e nulidade.</li>
            <li><strong>Geração de Modelos</strong>: As tabelas introspectadas são passadas para um template Jinja2, que gera automaticamente os modelos Sequelize no formato <code>.js</code>.</li>
            <li><strong>Criação Automática dos Arquivos</strong>: Para cada tabela do banco de dados, é gerado um arquivo <code>.js</code> dentro da pasta <strong>/models</strong>, contendo a definição do modelo Sequelize pronto para uso.</li>
        </ol>
        <h2>Pré-requisitos ⚙️</h2>
        <h3>Dependências Python:</h3>
        <p>O projeto requer algumas bibliotecas Python para funcionar corretamente. Para instalá-las, execute:</p>
        <pre><code>pip install sqlalchemy pymysql jinja2</code></pre>
        <h3>Dependências Node.js:</h3>
        <p>Para que os arquivos gerados funcionem no seu projeto Node.js com Sequelize, você precisará instalar as seguintes dependências:</p>
        <pre><code>npm install sequelize mysql2</code></pre>
        <h2>Configuração 🔧</h2>
        <p>No arquivo <strong>main.py</strong>, ajuste a URL de conexão com o banco de dados para corresponder às suas credenciais:</p>
        <pre><code>connection_url = "mysql+pymysql://usuario:senha@host:porta/nome_do_banco"</code></pre>
        <p>Substitua <code>usuario</code>, <code>senha</code>, <code>host</code>, <code>porta</code> e <code>nome_do_banco</code> com os valores corretos do seu banco de dados.</p>
        <h2>Como Rodar 🚀</h2>
        <ol>
            <li>Certa-se de que as dependências Python e Node.js estão instaladas.</li>
            <li>Execute o script <strong>main.py</strong>:</li>
        </ol>
        <pre><code>python main.py</code></pre>
        <p>O script se conectará ao banco de dados, lerá as tabelas, e gerará arquivos de modelo <code>.js</code> na pasta <strong>/models</strong>.</p>
        <h3>Exemplo</h3>
        <p>Se o banco de dados tiver uma tabela chamada <code>users</code>, o script irá gerar um arquivo <code>users.js</code> com o seguinte conteúdo:</p>
        <pre><code>
const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const User = sequelize.define('User', {
    id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        primaryKey: true,
    },
    name: {
        type: DataTypes.STRING,
        allowNull: true,
    },
    email: {
        type: DataTypes.STRING,
        allowNull: true,
    }
}, {
    tableName: 'users',
    timestamps: false
});

module.exports = User;
        </code></pre>
        <h2>Testes 🧪</h2>
        <p>Para testar o projeto e garantir que os modelos estão sendo gerados corretamente:</p>
        <ol>
            <li>Verifique se o banco de dados está acessível e que as credenciais no arquivo <strong>main.py</strong> estão corretas.</li>
            <li>Execute o script e confira os arquivos <code>.js</code> gerados na pasta <strong>/models</strong>.</li>
            <li>Teste os modelos gerados em um projeto Node.js com Sequelize, realizando consultas nas tabelas.</li>
        </ol>
    </div>
</body>
</html>
