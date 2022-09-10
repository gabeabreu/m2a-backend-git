from empresa.models import EmpresaMaster
from endereco.models import Endereco
from faturamento.models import Faturamento
from fundamento.models import Fundamento
from pergunta.models import Pergunta
from resposta.models import Resposta
from segmento.models import Segmento
from setor.models import Setor
from tipo_diagnostico.models import TipoDiagnostico
from tipo_industria.models import TipoIndustria
from uf.models import Uf
from valor_arrecadacao.models import ValorArrecadacao


def seed_uf():
    Uf.objects.all().delete()
    Uf.objects.bulk_create([
        Uf(1, 'AC', 'Acre'),
        Uf(2, 'AL', 'Alagoas'),
        Uf(3, 'AP', 'Amapá'),
        Uf(4, 'AM', 'Amazonas'),
        Uf(5, 'BA', 'Bahia'),
        Uf(6, 'CE', 'Ceará'),
        Uf(7, 'DF', 'Distrito Federal'),
        Uf(8, 'ES', 'Espírito Santo'),
        Uf(9, 'GO', 'Goiás'),
        Uf(10, 'MA', 'Maranhão'),
        Uf(11, 'MT', 'Mato Grosso'),
        Uf(12, 'MS', 'Mato Grosso do Sul'),
        Uf(13, 'MG', 'Minas Gerais'),
        Uf(14, 'PA', 'Pará'),
        Uf(16, 'PB', 'Paraíba'),
        Uf(17, 'PR', 'Paraná'),
        Uf(18, 'PE', 'Pernambuco'),
        Uf(19, 'PI', 'Piauí'),
        Uf(20, 'RJ', 'Rio de Janeiro'),
        Uf(21, 'RN', 'Rio Grande do Norte'),
        Uf(22, 'RS', 'Rio Grande do Sul'),
        Uf(23, 'RO', 'Rondônia'),
        Uf(24, 'RR', 'Roraima'),
        Uf(25, 'SC', 'Santa Catarina'),
        Uf(26, 'SP', 'São Paulo'),
        Uf(27, 'SE', 'Sergipe'),
        Uf(28, 'TO', 'Tocantins'),
        Uf(29, 'NA', 'Estrangeiro'),
    ])


def seed_setor():
    Setor.objects.all().delete()
    Setor.objects.bulk_create([
        Setor(1, 'Agronegócio'),
        Setor(2, 'Análise Clínica'),
        Setor(3, 'Comércio'),
        Setor(4, 'Indústria'),
        Setor(5, 'Micro e Pequenas Empresas'),
        Setor(6, 'Serviços'),
        Setor(7, 'Serviços de Tecnologia da Informação'),
        Setor(8, 'Serviços de Turismo'),
        Setor(9, 'Serviços Financeiros'),
        Setor(10, 'Outro'),
    ])


def seed_segmento():
    Segmento.objects.all().delete()
    Segmento.objects.bulk_create([
        Segmento(1, 'Adestramento'),
        Segmento(2, 'Agrícultura e Pesca'),
        Segmento(3, 'Agroenergia'),
        Segmento(4, 'Agronegócio'),
        Segmento(5, 'Alimentação'),
        Segmento(6, 'Aluguel de Espaço Físico'),
        Segmento(7, 'Apicultura'),
        Segmento(8, 'Artesanato'),
        Segmento(9, 'Biotecnologia'),
        Segmento(10, 'Borracharia'),
        Segmento(11, 'Café'),
        Segmento(12, 'Carne'),
        Segmento(13, 'Comércio Varejista'),
        Segmento(14, 'Construção Civil'),
        Segmento(15, 'Consultoria Comercial'),
        Segmento(16, 'Consultoria Empresarial'),
        Segmento(17, 'Cosméticos'),
        Segmento(18, 'Couro e Calçados'),
        Segmento(19, 'Cultura e Entretenimento'),
        Segmento(20, 'Derivados de Cana'),
        Segmento(21, 'Economia Criativa'),
        Segmento(22, 'Estética'),
        Segmento(23, 'Fabr. de Prod. de Padaria e Confeitaria'),
        Segmento(24, 'Floricultura'),
        Segmento(25, 'Fruticultura'),
        Segmento(26, 'Horticultura'),
        Segmento(27, 'Leite e Derivados'),
        Segmento(28, 'Madeira e Móveis'),
        Segmento(29, 'Mandiocultura'),
        Segmento(30, 'Material de Construção'),
        Segmento(31, 'MEI'),
        Segmento(32, 'Metal Mecânica'),
        Segmento(33, 'Moda'),
        Segmento(34, 'Não Informado'),
        Segmento(35, 'Ovinocaprinocultura'),
        Segmento(36, 'Pet Shop'),
        Segmento(37, 'Petróleo e Gás'),
        Segmento(38, 'Pizzaria'),
        Segmento(39, 'Química e Plásticos'),
        Segmento(40, 'Rochas Ornamentais'),
        Segmento(41, 'Salão de Beleza'),
        Segmento(42, 'Serviços'),
        Segmento(43, 'Serviços Financeiros'),
        Segmento(44, 'Serviços Médicos'),
        Segmento(45, 'Sindicato'),
        Segmento(46, 'Tecnologia da Informação'),
        Segmento(47, 'Têxtil e Confecções'),
        Segmento(48, 'Turismo'),
        Segmento(49, 'Outro'),
    ]),


def seed_valorArrecadacao():
    ValorArrecadacao.objects.all().delete()
    ValorArrecadacao.objects.bulk_create([
        ValorArrecadacao(1, 'MEI - até R$ 81.000'),
        ValorArrecadacao(2, '0 até R$ 360.000'),
        ValorArrecadacao(3, 'R$ 360.000 até R$ 4.800.000'),
        ValorArrecadacao(4, 'Acima de R$ R$ 4.800.000'),
    ])


def seed_tipoIndustria():
    TipoIndustria.objects.all().delete()
    TipoIndustria.objects.bulk_create([
        TipoIndustria(1, 'Associação/Cooperativa'),
        TipoIndustria(2, 'Cliente'),
        TipoIndustria(3, 'Filial'),
        TipoIndustria(4, 'Fornecedor'),
        TipoIndustria(5, 'Franquia'),
        TipoIndustria(6, 'Matriz'),
        TipoIndustria(7, 'Outros'),
    ])


def seed_fundamento():
    Fundamento.objects.all().delete()
    Fundamento.objects.bulk_create([
        Fundamento(1, 'Clientes'),
        Fundamento(2, 'Sociedade'),
        Fundamento(3, 'Liderança'),
        Fundamento(4, 'Estratégias e planos'),
        Fundamento(5, 'Pessoas'),
        Fundamento(6, 'Processos'),
        Fundamento(7, 'Informação e conhecimento'),
    ])


def seed_endereco():
    Endereco.objects.all().delete()
    Endereco.objects.bulk_create([
        Endereco(1, '000000', uf=Uf.objects.get(id=1))])


def seed_empresa():
    EmpresaMaster.objects.all().delete()
    EmpresaMaster.objects.bulk_create([
        EmpresaMaster(1, '1', 'Vazio', 'Vazio', 1, '2022-06-18', 1,
                      segmento=Segmento.objects.get(id=1),
                      setor=Setor.objects.get(id=1),
                      tipo_industria=TipoIndustria.objects.get(id=1),
                      faturamento=Faturamento.objects.get(id=1),
                      endereco=Endereco.objects.get(id=1),
                      valor_arrecadacao=ValorArrecadacao.objects.get(id=1))
    ])


def seed_resposta():
    Resposta.objects.all().delete()
    Resposta.objects.bulk_create([
        Resposta(
            1,
            'Não é feito nenhuma separação/segmentação/agrupamento de clientes',
            4),
        Resposta(2,
                 'A separação/segmentação/agrupamento é feito de forma intuitiva sem definição clara dos tipos de clientes',
                 3),
        Resposta(
            3,
            'A separação/segmentação/agrupamento é feito de forma planejada utilizando dados dos clientes',
            2),
        Resposta(4,
                 'A separação/segmentação/agrupamento é feito de forma planejada e as informações são utilizadas para melhor atender os clientes atuais e captar novos',
                 1),
        Resposta(
            5,
            'As necessidades e expectativas dos clientes não são conhecidas',
            4),
        Resposta(
            6,
            'As necessidades e expectativas dos clientes são conhecidas de forma intuitiva',
            3),
        Resposta(
            7,
            'As necessidades e expectativas dos clientes são conhecidas com base em informações dos clientes',
            2),
        Resposta(8,
                 'As necessidades e expectativas dos clientes são conhecidas, com base em informações dos clientes, utilizando métodos formalizados',
                 1),
        Resposta(9, 'Os serviços e produtos não são divulgados', 4),
        Resposta(
            10,
            'Os serviços e produtos são divulgados sem considerar os diferentes tipos de clientes',
            3),
        Resposta(
            11,
            'Os serviços e produtos são divulgados para alguns tipos de clientes',
            2),
        Resposta(12,
                 'Os serviços e produtos são divulgados considerando os diferentes tipos de clientes e o canal mais adequado para atingi-los',
                 1),
        Resposta(
            13, 'Não há um canal de recebimento das reclamações dos clientes',
            4),
        Resposta(
            14,
            'As reclamações não são registradas, sendo resolvidas, ocasionalmente, conforme a sua gravidade',
            3),
        Resposta(15, 'As reclamações são registradas e resolvidas', 2),
        Resposta(
            16,
            'As reclamações são registradas, resolvidas e é dado retorno ao cliente',
            1),
        Resposta(
            17,
            'Não há um canal de recebimento para os clientes informarem o nível de satisfação',
            4),
        Resposta(18,
                 'O nível de satisfação dos clientes não são registrados, porém, ocasionalmente são resolvido conforme a sua gravidade',
                 3),
        Resposta(19, 'O nível de satisfação é registrado e resolvido', 2),
        Resposta(
            20,
            'O nível de satisfação é registrado, resolvido e é dado retorno ao cliente',
            1),
        Resposta(21, 'Os impactos negativos não são conhecidos', 4),
        Resposta(
            22,
            'Algumas ações são tomadas, mas os impactos negativos não são conhecidos',
            3),
        Resposta(
            23,
            'Os impactos negativos são conhecidos e algumas ações são tomadas para tratá-los',
            2),
        Resposta(
            24,
            'Os impactos negativos são identificados e tratados de forma planejada',
            1),
        Resposta(25, 'As exigências legais necessárias não são conhecidas', 4),
        Resposta(
            26,
            'Algumas exigências legais necessárias são conhecidas, mas não são mantidas atualizadas',
            3),
        Resposta(
            27,
            'As exigências legais necessárias são conhecidas, mas não são mantidas atualizadas',
            2),
        Resposta(
            28,
            'Todas as exigências legais são conhecidas e mantidas atualizadas',
            1),
        Resposta(29, 'Não são realizadas ações e/ou projetos sociais', 4),
        Resposta(
            30,
            'Ações sociais são realizadas, sem o envolvimento dos colaboradores',
            3),
        Resposta(
            31,
            'Ações sociais são realizadas, com o envolvimento dos colaboradores',
            2),
        Resposta(32,
                 'Projetos sociais, que promovem o desenvolvimento local e regional, são realizados e têm o envolvimento dos colaboradores',
                 1),
        Resposta(33, 'A missão e valores não estão definidos', 4),
        Resposta(
            34,
            'A missão e valores estão definidos informalmente, sendo de conhecimento apenas dos dirigentes',
            3),
        Resposta(
            35,
            'A missão e valores estão escritos e é do conhecimento de alguns colaboradores',
            2),
        Resposta(
            36,
            'A missão e valores estão escritos e é do conhecimento de todos os colaboradores',
            1),
        Resposta(
            37,
            'Não há definição de regras para assegurar o comportamento ético',
            4),
        Resposta(
            38,
            'O comportamento ético é promovido por meio de regras informais',
            3),
        Resposta(
            39,
            'O comportamento ético está explicado como um dos valores da empresa',
            2),
        Resposta(40,
                 'O comportamento ético está detalhado em regras escritas que são do conhecimento de todos os colaboradores',
                 1),
        Resposta(41, 'Não há análise do desempenho do negócio', 4),
        Resposta(
            42,
            'A análise do desempenho do negócio é feita ocasionalmente com foco principalmente financeiro',
            3),
        Resposta(43,
                 'A análise do desempenho do negócio é feita regularmente com uso de indicadores restritos aos aspectos de vendas, financeiro e produção',
                 2),
        Resposta(44,
                 'Há reuniões regulares para a análise do desempenho com uso de indicadores abrangentes ao negócio(vendas, fornecedores, clientes, colaboradores, financeiro, produção e aspectos ambientais) ',
                 1),
        Resposta(
            45, 'Não há compartilhamento de informações com os colaboradores',
            4),
        Resposta(46,
                 'O compartilhamento de informações ocorre esporadicamente',
                 3),
        Resposta(
            47,
            'O compartilhamento de informações ocorre regularmente e abrange alguns colaboradores',
            2),
        Resposta(
            48,
            'O compartilhamento de informações ocorre regularmente e abrange todos os colaboradores ',
            1),
        Resposta(49, 'Não investe em seu desenvolvimento', 4),
        Resposta(50,
                 'Investe esporadicamente em seu desenvolvimento, mas não aplica os conhecimentos adquiridos na empresa',
                 3),
        Resposta(
            51,
            'Investe esporadicamente em seu desenvolvimento e aplica os conhecimentos adquiridos na empresa',
            2),
        Resposta(
            52,
            'Investe regularmente em seu desenvolvimento e aplica os conhecimentos adquiridos na empresa ',
            1),
        Resposta(53, 'As melhorias não são promovidas', 4),
        Resposta(54,
                 'As melhorias são promovidas em conseqüência de problemas',
                 3),
        Resposta(55,
                 'As melhorias são promovidas regularmente a partir de contribuições de colaboradores e de informações obtidas externamente',
                 2),
        Resposta(56,
                 'As melhorias são promovidas regularmente a partir de contribuições de colaboradores e de informações obtidas externamente, existindo dentre as melhorias pelo menos um exemplo de uma inovação implementada na empresa ',
                 1),
        Resposta(57, 'A visão não está definida', 4),
        Resposta(
            58,
            'A visão está definida informalmente, sendo de conhecimento apenas dos dirigentes',
            3),
        Resposta(
            59,
            'A visão está escrita e é do conhecimento de alguns colaboradores',
            2),
        Resposta(
            60,
            'A visão está escrita e é do conhecimento de todos os colaboradores ',
            1),
        Resposta(61, 'As estratégias não estão definidas', 4),
        Resposta(
            62,
            'As estratégias estão definidas na forma de intenções e idéias restritas aos dirigentes',
            3),
        Resposta(63,
                 'As estratégias estão definidas informalmente levando em consideração informações internas e externas',
                 2),
        Resposta(64,
                 'As estratégias definidas formalmente por meio de método que leva em consideração informações internas e externas',
                 1),
        Resposta(
            65,
            'Os indicadores relacionados às estratégias não são estabelecidos',
            4),
        Resposta(66,
                 'Os indicadores são estabelecidos para algumas estratégias',
                 3),
        Resposta(
            67,
            'Os indicadores e suas metas são estabelecidos para algumas estratégias',
            2),
        Resposta(68,
                 'Os indicadores e suas metas são estabelecidos para as principais estratégias e são disseminados para os colaboradores',
                 1),
        Resposta(69, 'Os planos de ação não são definidos', 4),
        Resposta(
            70,
            'As ações são definidas informalmente para o alcance de algumas metas',
            3),
        Resposta(
            71,
            'Os planos de ação são elaborados para o alcance das principais metas',
            2),
        Resposta(72,
                 'Os planos de ação são elaborados para o alcance das principais metas e são acompanhados por um responsável',
                 1),
        Resposta(73, 'Não estão definidas', 4),
        Resposta(74, 'Estão definidas informalmente', 3),
        Resposta(
            75,
            'Estão documentadas e conhecidas pela maioria dos colaboradores',
            2),
        Resposta(76,
                 'Estão documentadas e conhecidas por todos os colaboradores',
                 1),
        Resposta(77, 'Não leva em conta as necessidades da empresa', 4),
        Resposta(
            78,
            'Leva em conta as necessidades mínimas para o cargo, mas para apenas algumas funções',
            3),
        Resposta(79,
                 'Leva em conta as necessidades para o cargo para a maioria das funções, mas é feita informalmente e sem um padrão definido',
                 2),
        Resposta(80,
                 'Leva em conta as necessidades para o cargo para a maioria das funções e é feita com um padrão definido',
                 1),
        Resposta(81, 'Não são oferecidas ações de capacitações', 4),
        Resposta(
            82,
            'São oferecidas ações de capacitação para alguns colaboradores',
            3),
        Resposta(
            83,
            'São oferecidas ações de capacitação para a maioria dos colaboradores',
            2),
        Resposta(84,
                 'São disponibilizadas ações de capacitação para a maioria dos colaboradores com base num plano de treinamento',
                 1),
        Resposta(85, 'Os perigos e riscos não são conhecidos', 4),
        Resposta(
            86,
            'Alguns riscos são tratados, mas os perigos não estão identificados de forma adequada',
            3),
        Resposta(87,
                 'Os perigos são identificados, por meio de métodos que incluem PPRA e PCMSO, e os riscos tratados apenas com ações corretivas',
                 2),
        Resposta(88,
                 'Os perigos são identificados por meio de métodos que incluem PPRA e PCMSO, e os riscos tratados com ações corretivas',
                 1),
        Resposta(89, 'Não existem ações para o bem-estar dos colaboradores',
                 4),
        Resposta(
            90, 'São adotadas ações apenas quando os problemas são detectados',
            3),
        Resposta(91,
                 'São adotadas ações decorrentes de uma análise informal da satisfação dos colaboradores com o ambiente de trabalho',
                 2),
        Resposta(92,
                 'São adotadas ações decorrentes de uma análise formal da satisfação dos colaboradores com o ambiente de trabalho',
                 1),
        Resposta(
            93,
            'As atividades não são executadas de acordo com os padrões definidos',
            4),
        Resposta(
            94,
            'Algumas atividades são executadas de acordo com padrões definidos, mas não documentados',
            3),
        Resposta(95,
                 'As principais atividades são executadas de acordo com padrões documentados definidos a partir dos requisitos',
                 2),
        Resposta(96,
                 'As principais atividades são executadas de acordo com padrões documentados definidos a partir dos requisitos e de uma descrição de processo (fluxo e etc)',
                 1),
        Resposta(97, 'As atividades e o desempenho não são controlados', 4),
        Resposta(
            98,
            'As atividades e o desempenho são controlados quando ocorrem problemas',
            3),
        Resposta(99,
                 'Algumas atividades e o desempenho são controlados tomando como base os padrões de execução definidos',
                 2),
        Resposta(100,
                 'As principais atividades e o desempenho são controlados tomando como base os padrões de execução definidos, sendo algumas delas controladas por meio de indicadores e metas',
                 1),
        Resposta(101, 'Não é feita a seleção de fornecedores', 4),
        Resposta(
            102,
            'Os fornecedores são selecionados com critérios definidos, mas o desempenho não é avaliado',
            3),
        Resposta(103,
                 'Os fornecedores são selecionados com critérios definidos e o desempenho é avaliado quando ocorre algum problema',
                 2),
        Resposta(104,
                 'Os fornecedores são selecionados com critérios definidos e o desempenho é avaliado periodicamente, gerando ações para a sua melhorias sempre que necessário',
                 1),
        Resposta(105, 'Não há controles financeiros', 4),
        Resposta(
            106,
            'Há controles financeiros, mas não é utilizado fluxo de caixa', 3),
        Resposta(
            107, 'Há controles financeiros com a utilização de fluxo de caixa',
            2),
        Resposta(108,
                 'Há controles financeiros com a utilização de fluxo de caixa e um plano orçamentário com um horizonte de pelo menos um ano',
                 1),
        Resposta(109, 'As informações não estão agrupadas', 4),
        Resposta(
            110,
            'Algumas informações para a análise e execução das atividades estão definidas',
            3),
        Resposta(
            111,
            'As informações para a execução das atividades e análise e condução do negócio estão definidas',
            2),
        Resposta(112,
                 'As informações para a execução das atividades e análise e condução do negócio estão definidas e organizadas por um sistema de informação',
                 1),
        Resposta(113, 'As informações não são disponibilizadas', 4),
        Resposta(
            114,
            'As informações são disponibilizadas para alguns colaboradores',
            3),
        Resposta(
            115,
            'As informações são disponibilizadas para a maioria dos colaboradores',
            2),
        Resposta(116,
                 'As informações são disponibilizadas para os colaboradores, sendo documentadas e organizadas para a retenção do conhecimento na empresa',
                 1),
        Resposta(117, 'As informações de outras empresas não são conhecidas',
                 4),
        Resposta(
            118,
            'As informações de outras empresas são conhecidas, mas não utilizadas',
            3),
        Resposta(
            119,
            'As informações de outras empresas são conhecidas e utilizadas ocasionalmente',
            2),
        Resposta(
            120,
            'As informações de outras empresas são conhecidas e utilizadas regularmente',
            1),
    ])


def seed_pergunta():
    Pergunta.objects.all().delete()
    Pergunta.objects.bulk_create([
        Pergunta(1,
                 'Sr. Empresário, a sua empresa p',
                 'O agrupamento dos clientes tem ',
                 '', 1, [1, 2, 3, 4]),
        Pergunta(2,
                 'Sr. Empresário, a sua empresa possui algum método para realizar o levantamento de informações para conhecer necessidades e expectativas dos seus clientes?',
                 'A identificação, a análise e a compreensão das necessidades e expectativas dos clientes-alvo visam obter as informações necessárias para a configuração de serviços e produtos, que incorporem as características mais relevantes para os grupos de clientes.',
                 '', 1, [5, 6, 7, 8]),
        Pergunta(3,
                 'Sr. Empresário, a sua empresa possui algum método para realizar a divulgação dos seus produtos e serviços aos seus clientes e ao mercado?',
                 'A divulgação dos produtos tem a finalidade de despertar o interesse dos clientes atuais e potenciais nos segmentos de mercado pelos produtos de empresa.',
                 '', 1,
                 [9, 10, 11, 12]),
        Pergunta(4,
                 'Sr. Empresário, a sua empresa possui algum método para tratar as reclamações feitas pelos seus clientes?',
                 'O tratamento das reclamações, de forma pronta e eficaz, tem a finalidade de eliminar falhas em serviços e produtos, melhorando suas características. Objetiva, também, melhorar os níveis de satisfação e de fidelização dos clientes.',
                 '', 1,
                 [13, 14, 15, 16]),
        Pergunta(5,
                 'Sr. Empresário, a sua empresa possui algum método para avaliar o nível de satisfação dos seus clientes e do mercado referente aos seus produtos e/ou serviços?',
                 'A avaliação da satisfação dos clientes tem por objetivo mensurar sua percepção sobre a empresa, seus serviços e produtos, identificando oportunidades para a melhoria. Ex: existe alguma forma de avaliar a satisfação dos clientes?',
                 '', 1,
                 [17, 18, 19, 20]),
        Pergunta(6,
                 'Sr. Empresário, todo negócio/empresa gera algum tipo de impacto negativo ao meio ambiente. A sua empresa possui algum método para tratar esses impactos?',
                 'Para que a empresa possa tratar seus impactos ambientais é necessário que, primeiramente, conheça os danos que suas atividades e instalações causam ao meio ambiente.',
                 '', 2,
                 [21, 22, 23, 24]),
        Pergunta(7,
                 'Sr. Empresário, você conhece quais são as exigências legais para o funcionamento do seu negócio? Você procura se atualizar sempre em relação a essas exigências legais?',
                 'As exigências legais são aquelas determinadas pela legislação vigente, sob o controle de órgão competente municipal, estadual e federal (MEC, vigilância Sanitária, órgão Ambiental, Procon, etc).',
                 '', 2,
                 [25, 26, 27, 28]),
        Pergunta(8,
                 'Sr. Empresário, sua empresa possui algum tipo de ação independente ou coletiva de participação em projeto social que beneficie, de alguma forma, a comunidade e/ou a sociedade?',
                 'As ações sociais, como doações que auxiliem temporariamente a comunidade, não geram o desenvolvimento sustentado. O desenvolvimento sustentado é promovido quando ocorre o crescimento econômico, social, humano e ambiental da comunidade.',
                 '', 2,
                 [29, 30, 31, 32]),
        Pergunta(9,
                 'Sr. Empresário, a sua empresa possui missão e valores definidos? Como essa missão e valores são repassados/divulgados para os colaboradores?',
                 'A definição da missão tem como finalidade deixar clara a razão de existir da empresa, assegurando a convergência nas ações de todas as pessoas. A definição dos valores tem como finalidade deixar claros os princípios que regem comportamentos e atitudes das pessoas na empresa. '
                 'Exemplos: confiança, ética, respeito ao meio ambiente e etc. A comunicação da missão e dos valores aos colaboradores tem como finalidade contribuir para que todos compartilhem e persigam os mesmos ideais, potencializando a contribuição de cada um na empresa.',
                 '', 3,
                 [33, 34, 35, 36]),
        Pergunta(10,
                 'Sr. Empresário, a sua empresa possui definido os valores éticos para serem seguidos pelos dirigentes e colaboradores no ambiente interno e externo?',
                 'O tratamento das questões éticas visa promover o relacionamento ético entre as pessoas da empresa e nas relações externas com clientes, fornecedores, concorrentes e governo.',
                 '', 3,
                 [37, 38, 39, 40]),
        Pergunta(11,
                 'Sr. Empresário, sua empresa possui algum método para analisar o desempenho do negócio e dos colaboradores?',
                 'A análise de desempenho do negócio é fundamental para que os dirigentes identifiquem se os objetivos/metas estão sendo alcançados. '
                 'Esta análise deve ser realizada com informações e indicadores relacionados não só aos aspectos financeiros e da produção, mas também relacionados a vendas, fornecedores, clientes, colaboradores, clientes, colaboradores, financeiro, produção e aspectos ambientais.',
                 '', 3,
                 [41, 42, 43, 44]),
        Pergunta(12,
                 'Sr. Empresário, sua empresa possui algum método para divulgar e/ou compartilhar informações com os colaboradores?',
                 'O compartilhamento de informações sobre a empresa com os colaboradores tem como finalidade desenvolver um sentimento coletivo de pertencer a um grupo de pessoas que perseguem os mesmos ideais, potencializando a contribuição de cada um. '
                 'Quando todos os colaboradores entendem quais são os objetivos da empresa e acompanha os resultados obtidos rumo ao cumprimento destes objetivos, a produtividade aumenta. Ex: mural, email, em reuniões, via email e se existe política de comunicação interna.',
                 '', 3,
                 [45, 46, 47, 48]),
        Pergunta(13,
                 'Sr. Empresário, sua empresa promove, incentiva e/ou patrocina de algum tipo de capacitação para o DESENVOLVIMENTO GERENCIAL? Como esses conhecimentos são aplicados na própria empresa?',
                 'A busca por conhecimentos gerenciais pelos dirigentes tem a finalidade de manter-se atualizado em relação às exigências do mercado na condução do negócio. '
                 'Ex: cursos, palestras, feiras, congresso (com ou sem a participação de colaboradores).',
                 '', 3,
                 [49, 50, 51, 52]),
        Pergunta(14,
                 'Sr. Empresário, sua empresa possui algum método para promover a melhoria dos produtos, serviços, processos e métodos de gestão?',
                 'A promoção de melhorias e a busca de inovação dos métodos de gestão, marketing, processos, serviços e produtos têm como finalidade aumentar a competitividade da empresa. '
                 'A melhoria pode ser buscada internamente, ouvindo os colaboradores, e externamente, por meio da interação com o ambiente externo, como, por exemplo: outras empresas, inclusive concorrentes, universidades, centros de pesquisas, associações, rede de relacionamentos, etc.',
                 '', 3,
                 [53, 54, 55, 56]),
        Pergunta(15,
                 'Sr. Empresário, sua empresa possui visão de futuro? Como ela é divulgada e compreendida pelos colaboradores?',
                 'A definição da visão tem como finalidade deixar claro o que os dirigentes esperam da empresa num futuro definido. Essa visão deverá nortear as ações do planejamento estratégico. '
                 'A comunicação da visão aos colaboradores tem como finalidade contribuir para que todos compartilhem e persigam os mesmos ideais, potencializando a contribuição de cada um na empresa.',
                 '', 4,
                 [57, 58, 59, 60]),
        Pergunta(16,
                 'Sr. Empresário, a empresa possui algum tipo de estratégia para alcançar a visão de futuro estabelecida pela empresa?',
                 'Ao definir a visão, a empresa deve estabelecer estratégias para alcançá-las e direcionar seus esforços. '
                 'Essas estratégias devem levar em conta informações relativas aos clientes, mercado, fornecedores, colaboradores, sua capacidade de prestar serviços, produzir e vender, para posicioná-la de forma competitiva e garantir a sua continuidade. Ex: planejamento estratégico anual, Plano de Marketing e entre outras.',
                 '', 4,
                 [61, 62, 63, 64]),
        Pergunta(17,
                 'Sr. Empresário, a empresa estabelece algum indicativo e/ou meta para as estratégias estabelecidas?',
                 'A definição dos indicadores tem o objetivo de permitir a avaliação do alcance das estratégias por meio de resultados quantitativos. O estabelecimento de metas para os indicadores visa definir níveis de resultados esperados para permitir a análise do desempenho do negócio. '
                 'Ex: quantos clientes pretendem conquistar, quanto do produto/serviço X quero vendar a mais e etc.',
                 '', 4,
                 [65, 66, 67, 68]),
        Pergunta(18,
                 'Sr. Empresário, a empresa possui algum método de planejamento para implementar as ações estratégicas definidas para atingir as metas estabelecidas? ex; plano de ação.',
                 'Os Planos de Ação são importantes ferramentas para desdobrar as estratégias de modo a atingir as metas. De modo geral, os planos de ação são estabelecidos para realizar aquilo que a empresa deve fazer para que sua estratégia seja bem-sucedida. '
                 'Ex: o plano ação define quem, aonde, como, prazo, custo e etc.',
                 '', 4,
                 [69, 70, 71, 72]),
        Pergunta(19,
                 'Sr. Empresário, sua empresa tem bem definidas as funções e responsabilidades dos dirigentes e/ou colaboradores?',
                 'A definição clara das funções e responsabilidades e seu conhecimento por todos da empresa têm a finalidade de esclarecer como deve ser a participação das pessoas,  promover a sinergia do trabalho em equipe e a eficiência e produtividade do sistema de trabalho como um todo. '
                 'Ex: existe política de RH, organograma e etc.', '', 5,
                 [73, 74, 75, 76]),
        Pergunta(20,
                 'Sr. Empresário, sua empresa possui algum método para realizar a contratação dos colaboradores?',
                 'A contratação de colaboradores tem como objetivo preencher as vagas da empresa com profissionais aptos para atender às necessidades atuais e futuras. '
                 'Pode considerar as oportunidades para o desenvolvimento de membros da equipe atual, assim como promover a inserção e integração de novas pessoas para o exercício das funções. '
                 'Ex: a empresa avalia o perfil da vaga e do colaborador ideal, a empresa avalia a possibilidade de aproveitar um colaborador interno, o meio para encontrar o colaborador ideal é colocação de anúncio, indicação e etc.',
                 '', 5,
                 [77, 78, 79, 80]),
        Pergunta(21,
                 'Sr. Empresário, sua empresa promove, incentiva e/ou patrocina algum tipo de capacitação para o desenvolvimento dos colaboradores?',
                 'A capacitação dos colaboradores tem por finalidade desenvolver as habilidades e conhecimento para que eles possam desenvolver suas atividades diárias, de forma a garantir a eficiência e a sinergia da equipe. '
                 'Ex: são oferecidos cursos, palestras, congressos, treinamentos pelos fornecedores e etc.',
                 '', 5,
                 [81, 82, 83, 84]),
        Pergunta(22,
                 'Sr. Empresário, a empresa possui algum método para identificar: perigos de acidentes, de saúde e/ou de segurança no ambiente de trabalho da empresa?',
                 'A identificação dos perigos e o tratamento dos riscos relacionados a saúde e segurança no trabalho têm como objetivo inventariar, priorizar e viabilizar o tratamento corretivo e preventivo dos fatores que possam ameaçar a integridade física ou psicológica dos integrantes da força de trabalho em decorrência de suas atividades.  '
                 'Ex: sua empresa atende as exigências PCMSO( Programa de Controle de Medicina e Saúde Ocupacional) e do PPRA(Programa de Prevenção de Riscos Ambientais).',
                 '', 5,
                 [85, 86, 87, 88]),
        Pergunta(23,
                 'Sr. Empresário, a empresa possui alguma forma de avaliar e tratar o bem-estar e satisfação dos colaboradores?',
                 'A doação de ações para garantir o bem-estar e a satisfação dos colaboradores tem como finalidade promover um ambiente de trabalho mais participativo e agradável que proporcione motivação para a realização do trabalho. '
                 'Estas ações podem incluir, por Ex: benefícios adicionais exigidos pela legislação, realização de atividades esportivas, confraternizações, áreas de lazer, facilidade de comunicação em todos os níveis entre outros.',
                 '', 5,
                 [89, 90, 91, 92]),
        Pergunta(24,
                 'Sr. Empresário, para que as atividades da empresa sejam executadas de maneira eficiente e padronizada, gostaria de saber se existe algum tipo de padrão de execução de tarefa documentado?',
                 'As atividades da empresa estão associadas à prestação de serviços, à comercialização e à produção de bens para atender às necessidades dos clientes. '
                 'O uso de padrões definidos e documentados assegura a uniformidade e continuidade da execução das atividades. Esses devem levar em consideração os requisitos, os quais são obtidos principalmente a partir de informações das necessidades dos clientes e da legislação. '
                 'Ex: manual de processos, registros de normas e padrões e etc.',
                 '', 6,
                 [93, 94, 95, 96]),
        Pergunta(25,
                 'Sr.Empresário, a empresa possui algum método para controlar as atividades e o seu desempenho?',
                 'O controle das atividades tem por finalidade assegurar que os requisitos definidos sejam atendidos, permitindo a tomada de medidas corretivas quando necessário. '
                 'O estabelecimento de metas para os indicadores visa definir os níveis de resultados esperados para os requisitos. Ex: produção, fornecedores, logística, estoque, vendas e etc',
                 '', 6,
                 [97, 98, 99, 100]),
        Pergunta(26,
                 'Sr. Empresário, a empresa possui algum método para selecionar e avaliar os seus fornecedores em relação ao seu desempenho?',
                 'A qualidade dos serviços prestados e produtos fornecidos aos clientes pela empresa depende da qualidade dos itens/serviços adquiridos de fornecedores. '
                 'Por isso, é importante que a empresa selecione e monitore o desempenho de seus fornecedores, com o objetivo de otimizar a qualidade e reduzir os custos de fornecimento.',
                 '', 6,
                 [101, 102, 103, 104]),
        Pergunta(27,
                 'Sr. Empresário, sabemos que o controle financeiro de uma empresa é fundamental para a sobrevivência, tomadas de decisões e sucesso. '
                 'Neste sentido gostaria de saber se a sua empresa possui algum método para realizar os controles financeiros afim de melhor utilizá-los?',
                 'A operação da empresa depende da disponibilidade de recursos financeiros para fazer frente a compras de serviços e materiais, para pagar empregados e despesas, e para investir em equipamentos necessários a comercialização, prestação de serviços ou a fabricação de produtos e sua entrega. '
                 'O monitoramento e o controle dos aspectos financeiros são essenciais para assegurar as operações. O plano financeiro orçamentário tem como finalidade fazer uma previsão das receitas, despesas e investimentos para assegurar a disponibilidade de recursos para a execução das atividades.',
                 '', 6,
                 [105, 106, 107, 108]),
        Pergunta(28,
                 'Sr. Empresário, a sua empresa possui algum método para definir quais informações são necessárias para a análise, execução das atividades e para a gestão do seu negócio?',
                 'A definição de sistemas de informação tem o objetivo de desenvolver e disponibilizar as ferramentas e tecnologias mais eficazes para atender às necessidades identificadas junto aos colaboradores. '
                 'Ex: existe aproveitamento das informações internas (vendas, comissões, logística, produção, estoque), fornecedor, concorrência e etc. ',
                 '', 7,
                 [109, 110, 111, 112]),
        Pergunta(29,
                 'Sr. Empresário, a sua empresa possui algum método para disponibilizar as informações para os colaboradores?',
                 'A disponibilização das informações, quando pertinente, tem como finalidade permitir a adequada operação e condução do negócio em todos os níveis. '
                 'A retenção do conhecimento da empresa, utilizando-se de registros, assegura a continuidade da operação em caso de substituição de pessoas.',
                 '', 7,
                 [113, 114, 115, 116]),
        Pergunta(30,
                 'Sr. Empresário, a sua empresa possui algum método para buscar informações de outras empresas com o objetivo de comparar e avaliar o desempenho e melhorar os serviços, produtos e processos da sua empresa?',
                 'A obtenção de informações comparativas inclui aquelas oriundas de empresa do seu ramo ou outros ramos de atividade e permite adotar novas práticas ou métodos para a melhoria dos serviços, produtos e processos. '
                 'Permite também a comparação de seus resultados, identificando diferenciais favoráveis e desfavoráveis a serem tratados.',
                 '', 7,
                 []),
    ])


def seed_tipo_diagnostico():
    TipoDiagnostico.objects.all().delete()
    TipoDiagnostico.objects.bulk_create([
        TipoDiagnostico(1, 'Completo'),
        TipoDiagnostico(2, 'Simples'),
    ])
