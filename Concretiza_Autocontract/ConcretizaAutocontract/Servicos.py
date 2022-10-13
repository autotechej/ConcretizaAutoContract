# -*- coding: utf-8 -*-
#encoding: utf-8
from datetime import datetime
import Functions as fct
now= datetime.now()
dataatual = now.strftime("%d/%m/%Y")
beta = 'Isso e um beta'
h1 = '{size: 54px; text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'
h2 = '{size: 40px; text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'
body = '{text-align: justify;\n\tmax-width: 650px;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;\n\tfont-size: 16px;\n\tpadding: 0;\n\tmargin: 0 auto !important;}'
h4 = '{size: 48px; text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'


def escrever_contrato():
    Contratohtml = open('.\Contrato.html', 'w', encoding='utf-8')
    Contratohtml.write(
        f'<!DOCTYPE>\n\t<html>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=297x420" initialscale="1">\n\t<title>Concretiza</title>\n\t<style>\n\th1 {h1}\n\th2 {h2}\n\th4 {h4}\n\tbody {body}\n\t</style>\n\t<head>\n\t<center>\n\t<img src="./Logo2.jpg" width="400" height="300"></center>\n\t<h2>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</h2></h3>\n\t</head>\n\t<body>\n\t <p>Pelo presente instrumento particular celebrado na melhor forma de Direito e consoante todas as disposições legais pertinentes à matéria, de um lado a CONCRETIZA, - Empresa Júnior do Curso de Engenharia Civil, Saneamento e Estradas do Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), associação civil de direito privado, sem fins lucrativos, inscrita no CNPJ sob o nº 30.952.599/0001-24, com sede na Av. Treze de Maio, 2081, CEP 60170250 Centro, Fortaleza, Ceará, neste ato representada por intermédio de Larissa Alves Muniz Bezerra brasileira, solteira, maior, estudante, inscrito no o CPF nº 068.094.463.03, portador do RG nº 2005015056009, órgão expedidor SSP, residente e domiciliado à Rua Artur Bandeira n° 72-CEP 62870-000, Fortaleza, Ceará, Brasil, doravante denominada <strong>CONTRATADA</strong> e, de outro, a pessoa jurídica <strong>{fct.NomeEmpresa}</strong>  inscrita no CNPJ sob o n° {fct.CNPJCliente}, com sede à {fct.EnderecoCliente}, CEP: {fct.CEPcliente}, {fct.CidadeEstadoCliente}, neste ato representada por intermédio de <strong>{fct.NomeRepresentante}</strong>, brasileiro(a), {fct.EstadoCivilRepresentante}, maior, {fct.CargoRepresentante}, inscrito no CPF sob o n° {fct.CPFRepresentante} portador do RG nº {fct.RGRepresentante}, órgão expedidor:{fct.OrgaoExpedidor} residente e domiciliado em {fct.EnderecoCliente}, telefone n°: {fct.TelefoneRepresentante}, e email: {fct.EMAILCliente},doravante denominada <strong>CONTRATANTE</strong>, resolvem de comum acordo firmar o presente <strong>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</strong>, a ser regulado pelas cláusulas e condições abaixo lançadas que reciprocamente se obrigam.</p>\n<h4>DO OBJETO CONTRATUAL</h4>\n<p><strong>Cláusula 1ª.</strong> O objeto do presente instrumento de contrato consiste na prestação do(s) seguinte(s) serviço(s) abaixo delineado(s) por parte da <strong>CONTRATADA</strong> à <strong>CONTRATANTE:</strong>\n<ul><strong>I.</strong>serviço: {fct.DescricaoServico}<strong><p>II.</strong> serviço:{fct.DescricaoServico2}</p></ul> <p><strong> §1º</strong>.As informações contendo as especificações do serviço estarão contidas na proposta de projeto enviada e assinada pela <strong> CONTRATANTE</strong>, configurando-se como termo anexo e inseparável do presente contrato.</p>\n<p><strong>§2°</strong>.Os serviços solicitados à<strong> CONTRATADA</strong>, não apresentados nesta cláusula ou na proposta comercial, serão tidos como extraordinários  ou atividades especiais, ensejando a cobrança de honorários adicionais, conforme a cláusula.</p>\n<h4> DOS SERVIÇOS</h4>\n<p><strong>Cláusula 2ª</strong>.O serviço contratado será prestado pela<strog> CONTRATADA</strong> com total autonomia, liberdade de horário, sem pessoalidade, sem subordinação à <strong>CONTRATANTE</strong> e sem qualquer exclusividade, desde que não haja conflito de interesses.</p><br><br><p><strong>Cláusula 3ª.</strong> Os serviços a que faz menção o presente contrato, de responsabilidade da <strong>CONTRATADA</strong>, serão prestados por intermédio de seus membros e colaboradores.</p><p><strong>Cláusula 4ª.</strong>Todo e qualquer tipo de subcontratação realizada pela <strong>CONTRATADA</strong> deverá ter a devida autorização da parte<strong> CONTRATANTE</strong>.</p><h4>DAS OBRIGRAÇÕES </h4><p><strong>Cláusula 5ª.</strong>Compete à <strong> CONTRATADA:</strong><ul><strong>I.</strong>Prestar os serviços contratados na forma e modo ajustados pelas partes, dentro das normas e especificações técnicas declaradas e aplicáveis ao serviço, estabelecidas sob o critério da <strong>CONTRATADA</strong><p><strong>II.</strong>Entregar à <strong>CONTRATANTE</strong> cópia do presente Instrumento, que contém a Proposta Comercial, o cronograma e a tecnologia empregada, assinado pelas partes;<p><strong>III.</strong>Dirimir toda e qualquer dúvida a respeito do Serviço prestado e do presente contrato;</p><p><strong>IV.</strong>Cumprir o prazo estipulado no presente contrato para a efetiva entrega do serviço;</p><p><strong>V.</strong>Cobrar material ou informação ausentes necessários para realização do serviço com êxito por meio de comunicado oficial a ser enviado para o e-mail constante nocabeçalho deste contrato;</p><p><strong>VI.</strong>Fornecer à<strong> CONTRATANTE</strong> um serviço transparente e de qualidade;</p><p><strong>VII.</strong>Empregará parte de seu corpo técnico para a realização de pesquisa e desenvolvimento na área assessorada, bem como para a solução e prevenção de eventuais problemas, nomeando um responsável para a administração das atividades; </p><p><strong>VIII.</strong>Não se responsabilizar por quaisquer modificações realizadas no objeto do presente contrato sem consulta a ela feita ou sem sua aprovação prévia, tampouco as eventuais consequências dessas modificações.</p></ul><p><strong> Cláusula 6ª.</strong>Compete à<strong> CONTRATANTE:</strong></p><ul><strong>I.</strong>Receber os serviços executados e concluídos em estrita observância aos dados, prazos e especificações técnicas elencados no presente contrato;<<p><strong>II.</strong>Efetuar o pagamento na forma e modo aprazado, sob pena de rescisão contratual;</p><p><strong>III.</strong>Colocar à disposição da <strong>CONTRATADA </strong>as necessárias verbas pecuniárias para desenvolver o trabalho;</p><p><strong>IV.</strong>Fornecer à<strong> CONTRATADA</strong>  a documentação solicitada, ciente de que o atraso no envio do material ou da informação necessária para realização do serviço com êxito pode prejudicar o prazo de entrega do serviço, de modo que o prazo do contrato em questão ficará suspenso a contar do dia da comunicação oficial feita pela<strong> CONTRATADA;</strong></p><p><strong>V.</strong> Comunicar-se por meio do correio e/ou e-mail, com aviso de recebimento ao endereço constante no preâmbulo do presente documento, de forma a responsabilizar-se por atrasos na execução do acordado decorrentes de falhas que cause na comunicação;</p><p><strong>VI.</strong>Manter atualizados os meios de comunicação, informando à <strong>CONTRATADA</strong> eventuais mudanças de endereço, telefones de contato e endereço de correio eletrônico estabelecido no cabeçalho do presente contrato;</p><br><br><p><strong>VII.</strong>Proceder de modo que o serviço prestado ocorra na forma e modo estabelecido no cronograma de trabalho, considerando os seguintes pontos:</p><p><strong>a)</strong>Responder pelos resultados acordados com a equipe de consultores;</p><p><strong>b)</strong>Aprovar o relatório e entregas parciais;</p><p><strong>c)</strong>Efetuar os pagamentos devidos nas datas estipuladas;</p><p><strong>d)</strong>Fornecer todas as informações que forem solicitadas;</p><p><strong>e)</strong>Arcar com todas as despesas ordinárias e extraordinárias, bem como as administrativas que se fizerem, efetivamente, necessárias para a execução do serviço pela <strong>CONTRATADA;</strong></p><p><strong>f)</strong>Reconhecer que não terá nenhum direito, título ou interesse, por licença ou de outra forma, para usar os documentos ou informações obtidas, obrigando-se a não transmiti-los e nem revelá-los a terceiros, bem como a não discutir, usar, divulgar ou dispor deles, para outra finalidade que não aquela estritamente determinada no presente instrumento contratual.</p></ul>\n\t<h4>DO SIGILO E DO USO DE IMAGEM</h4>\n\t<p><strong>CLÁUSULA 7ª.</strong> A <strong>CONTRATADA</strong> se compromete a manter sigilo do que venha a ter acesso ou conhecimento acerca de materiais, especificações técnicas, financeiras ou comerciais, inovaçõesou aperfeiçoamentos da <strong>CONTRATANTE</strong>, e, ainda, do que lhe seja confiado em razão do desenvolvimento do objeto deste contrato, salvo se houver consentimento expresso por parte do <strong>CONTRATANTE</strong></p><p><strong>Parágrafo único.</strong> A <strong>CONTRATANTE</strong> autoriza desde já que a<strong> CONTRATADA</strong> utilize seu nome e imagem sobre o desenvolvimento do objeto do presente contrato para fins acadêmicos ou de divulgação como um dos projetos realizados pela<strong>CONTRATADA.</strong></p><p> \n\t<h4>DA VIGÊNCIA E DA ENTREGA</h4>\n\t<p><strong>CLÁUSULA 8ª.</strong> O presente contrato terá vigência de {fct.Vigencia}, salvo nas hipóteses de extinção contratual previstas no rol exemplificativo deste documento acordado entre as partes.</p><p><strong>CLÁUSULA 9ª.</strong>O Projeto {fct.DescricaoServico} será entregue em {fct.Prazo3}({fct.extenso3}) dias úteis após a aprovação expressa do Estudo Preliminar por parte do<strong> CONTRATANTE.</strong><p><strong>Cláusula 10ª.</strong>O prazo total do projeto será de {fct.DataFechamento}  dias úteis contados a partir do pagamento da entrada. Os prazos de cada etapa são estipulados entre as partes, podendo ser ajustados mediante as predisposições exposta nas cláusulas que versam sobre no presente contrato.</p> <p><strong>Cláusula 11ª.</strong>Caso a entrega, total ou parcialmente, não ocorra presencialmente, e sim por meios virtuais, cabe à<strong> CONTRATADA</strong> aguardar por até 24 horas do envio a confirmação de recebimento do <strong>CONTRATANTE</strong>. Após esse prazo, compromete-se a <strong>CONTRATADA</strong> a insistir na confirmação por, minimamente, 48 horas, quando fica autorizada a compreender que houve confirmação tácita. Passado o prazo, o serviço será considerado devidamente finalizado.</p> <p><strong>Cláusula 12ª.</strong>O projeto, impresso e em mídia digital, será entregue pela <strong>CONTRATADA</strong> à <strong>CONTRATANTE</strong>, respeitados todos os direitos estabelecidos em lei.<p><strong>Parágrafo único:</strong>Caso não haja modificações significativas após a primeira aprovação do cliente, o prazo para entrega final pode ser antecipado, desde que seja previamente</p><br><br><p>acordado entre as partes. Qualquer modificação exigida pelo <strong>CONTRATANTE</strong>  nas etapas citadas acima após sua aprovação expressa, mediante a sua assinatura, ficará sujeita a aditivos contratuais, caso o <strong> CONTRATADO</strong> julgue necessário. As mudanças dessa natureza e eventuais aditivos serão acordados previamente, assim como a prorrogação do prazo para cada modificação.</p>\n\t<h4>DO PRAZO</h4>\n\t<p><strong>CLÁUSULA 13ª.</strong>O prazo total do projeto será de {fct.Prazo3} ({fct.extenso3}) dias úteis contados a partir do pagamento da entrada. Os prazos de cada etapa são estipulados entre as partes, podendo ser ajustados mediante as predisposições expostas no presente contrato.</p><p><strong>§1º.</strong> Caso seja necessário o envio de material ou informação pela <strong>CONTRATANTE</strong> para realização do serviço pela <strong>CONTRATADA</strong>, o prazo estabelecido ficará SUSPENSO a partir do momento em que a <strong>CONTRATADA</strong> avisar da necessidade do material ou da informação de modo oficial, para o e-mail informado no cabeçalho deste contrato, até o momento em que a <strong>CONTRATANTE</strong> encaminhar o material ou a informação para a realização do serviço com efetividade.</p><p><strong>§2º.</strong>Caso haja atraso prolongado no pagamento pela<strong> CONTRATANTE</strong>sem justificativa prévia, o contrato ficará passível de suspensão por inadimplência até a efetuação do pagamento.</p><p><strong>§3º.</strong>Após a entrega do objeto instrumento do presente contrato, a <strong>CONTRATANTE</strong> terá um novo prazo de {fct.Prazo1} ({fct.extenso1}) dias úteis para comunicar-se com a <strong>CONTRATADA</strong>,  por meio de reunião presencial ou do veículo oficial de comunicação, na intenção de obter, em única solicitação, explicação ou requerer alguma alteração no serviço. A <strong>CONTRATADA</strong>,  por sua vez, terá o prazo de {fct.Prazo2} ({fct.extenso2})dias úteis para responder aos questionamentos da <strong>CONTRATANTE</strong> ou realizar as alterações solicitadas.</p><p><strong> §4º.</strong>Passados os prazos estabelecidos na presente cláusula, o serviço será considerado devidamente finalizado e a <strong>CONTRATADA</strong> não terá quaisquer obrigações de proceder às alterações solicitadas de forma intempestiva pela <strong>CONTRATANTE.</strong></p><p><strong>§5º.</strong> O pedido de explicação ou de alteração do instrumento deverá ser solicitado pelo meio de comunicação oficial escolhido pelas partes.</p><p><strong>Cláusula 14ª.</strong>O cronograma do projeto seguirá a seguinte ordem:</p><p>I.{fct.passo1}</p><p>II.{fct.passo2}</p><p>III.{fct.passo3}</p><p>IV.{fct.passo4}</p><p>V.{fct.passo5}</p><p><strong>Parágrafo único.</strong>O serviço contratado pode ser entregue antes do prazo planejado.</p><p><strong>Cláusula 15ª.</strong>O serviço contratado pode atrasar caso a<strong> CONTRATANTE </strong>não encaminhe de forma ágil o material ou a informação solicitada de modo oficial pela <strong>CONTRATADA.</strong> Nesse caso, a <strong>CONTRATADA</strong>estará completamente isenta de qualquer responsabilidade.</p>\n\t<h4>DO PAGAMENTO</h4>\n\t  <p><strong>Cláusula 16ª.</strong>.</p><br><br><p><strong>Cláusula 17ª.</strong>O pagamento deverá ser realizado {fct.DescricaoPagamento} à pessoa indicada pela <strong>CONTRATADA,</strong> por meio de boletos enviados pelo e-mail:{fct.EMAILCliente} ou por meio de depósito, seguido do envio do respectivo comprovante no canal de comunicação oficial, na conta corrente da <strong>CONTRATADA,</strong> cujos dados são:</p><p>Titular: {fct.Titular} </p><p>Banco: {fct.Banco} </p><p>Agência: {fct.Agencia} </p><p>Conta Corrente: {fct.Conta} </p><p>CNPJ: {fct.CNPJPagamento} </p>\n\t<h4>DA EXTINÇÃO DO CONTRATO</h4>\n\t<p><strong>CLÁUSULA 18ª</strong>.É assegurado às partes resilir o presente contrato antes do término do prazo.</p>\n\t<p><strong>§1º.</strong>. Caso a <strong>CONTRATANTE</strong>  decida pela resilição, deverá ser pago à<strong> CONTRATADA</strong>,o valor proporcional ao que já foi executado do serviço. Caso a <strong>CONTRATADA</strong> decida pela resilição, será devolvido parte do valor já pago, de maneira que também seja proporcional ao que já foi executado do serviço.</p><p><strong>§2º.</strong> Deverá ser notificada a intenção de resilir à parte contrária com antecedência mínima de 15 (quinze) dias, sob pena de multa de 10% (dez por cento) do valor total do contrato.</p><p><strong>§3º.</strong> O resultado do serviço será entregue à <strong>CONTRATANTE</strong>no formato em que estiver no momento da resilição.\n\t<p><strong>CLÁUSULA 19ª</strong>.Poderá o presente contrato ser considerado rescindido de pleno direito, independentemente de qualquer notificação ou interpelação, na hipótese de descumprimento de quaisquer de seus termos e condições, por ambas as partes, cabendo, contudo, penalidades à parte que der causa.</p><p><strong>§1º.</strong>Caso a <strong>CONTRATADA</strong> dê causa à rescisão, deverá devolver 30% (trinta por cento) dos valores já pagos até o momento pela<strong> CONTRATANTE.</strong><p><strong>§2º.</strong>Caso a<strong>  CONTRATANTE</strong> dê causa à rescisão deverá pagar o proporcional ao serviço já executado pela<strong> CONTRATADA</strong>, acrescido de uma multa de 10% (dez por cento) sobre o valor do contrato. \n\t<p><strong>CLÁUSULA 20ª</strong>.A eventual aceitação por uma das partes da inexecução pela outra de quaisquer cláusulas deste contrato, a qualquer tempo, deverá ser interpretada como mera liberalidade, não implicando, portanto, em novação ou na desistência de exigir o cumprimento das disposições aqui contidas ou do direito de pleitear, futuramente, a execução total de cada uma das obrigações.</p><p><strong>CLÁUSULA 21ª</strong>. A eventual aceitação por uma das partes da inexecução pela outra de quaisquer cláusulas deste contrato, a qualquer tempo, deverá ser interpretada como mera liberalidade, não implicando, portanto, em novação ou na desistência de exigir o cumprimento das disposições aqui contidas ou do direito de pleitear, futuramente, a execução total de cada uma das obrigações.</p>\n\t<br><br><br><br><h4>DA CONFIDENCIALIDADE.</h4>\n\t<p><strong>CLÁUSULA 22ª</strong>. Todos os relatórios eventualmente gerados no decorrer dos trabalhos são de propriedade integral da <strong>CONTRATADA,</strong> sendo vedado o seu uso ou divulgação para terceiros, ainda que parcial, sem sua prévia autorização.</p>\n\t<p><strong>Cláusula 23ª.</strong>Todos os dados, processos, técnicas, metodologias, tecnologia, know-how, marcas, patentes e quaisquer outros bens de propriedade intelectual da<strong> CONTRATADA</strong>, ou sobre os quais lhes convenha guardar sigilo, que venham, por elas, a ser disponibilizados para a execução deste contrato, permanecerão na respectiva titularidade, não podendo sobre eles haver vazamento de informações.</p>\n\t<p><strong>Parágrafo único.</strong> A violação desta Cláusula, mesmo depois de concluídos e pagos os serviços, sujeita à parte infratora, pelo prazo de 5 (cinco) anos, à indenização pelos danos que a quebra do sigilo vier a causar.</p>\n\t<h4>DAS DISPOSIÇÕES FINAIS</h4>\n\t<p><strong>Cláusula 24ª.</strong>O(s) meio(s) de comunicação oficial entre as partes será através de telefone e/ou email quais sejam: {fct.TelefoneRepresentante} e {fct.EMAILCliente}.</p><p><strong>Cláusula 25ª.</strong>Quaisquer mudanças não comunicadas à outra parte, que interfiram no cumprimento deste contrato, deverão ser compensadas pela parte responsável.</p><p><strong>Cláusula 26ª.</strong>A<strong> CONTRATANTE</strong> se responsabiliza, individualmente, pelo cumprimento das obrigações trabalhistas, previdenciárias e tributárias derivadas da relação existente entre si e seusempregados, servidores e/ou contratados, de forma que não se estabelecerá, em hipótese alguma, vínculo empregatício entre seus empregados, servidores e/ou contratados com a <strong>CONTRATADA,</strong> cabendo a cada uma a responsabilidade pela condução, coordenação e remuneração de seu pessoal.</p><p><strong>Cláusula 27ª.</strong>Toda e qualquer alteração contratual deverá ser feita através de Termo Aditivo, devidamente assinado e acordado pelas partes envolvidas, o qual será parte integrante e inseparável deste instrumento, sob pena de nulidade da alteração.</p><p><strong>Cláusula 28ª.</strong>A eventual aceitação por uma das partes da inexecução pela outra de quaisquer cláusulas deste contrato, a qualquer tempo, deverá ser interpretada como mera liberalidade, não implicando, portanto, em novação ou na desistência de exigir o cumprimento das disposições aqui contidas ou do direito de pleitear, futuramente, a execução total de cada uma das obrigações.</p><p><strong>Cláusula 29ª.</strong>As partes contratantes resguardam-se na exigência dos direitos e obrigações que lhe reservam o presente instrumento, ressalvados aqueles que venham a ferir a ética ou os princípios morais.</p><p><strong>Cláusula 30ª.</strong>Este instrumento de contrato serve como título executivo extrajudicial, nos termos do inciso III, art. 784, do Código de Processo Civil de 2015.</p><p><strong>Cláusula 31ª.</strong>A declaração de nulidade de qualquer cláusula ou item deste termo não prejudicará as demais, que continuarão em vigor e deverão ser integralmente cumpridas, desde que não inviabilize o cumprimento do objeto do presente contrato.</p><br><br><br><br><br><br>\n\t<h4>DO FORO</h4>\n\t<p><strong>Cláusula 32ª.</strong>Para a resolução de qualquer demanda judicial referente a eventual controvérsia ou omissão relativa ao presente contrato, excluídos quaisquer outros, fica eleito o foro da comarca de Fortaleza, Ceará.</p><p>E, por estarem assim ajustados, assinam este contrato, em 02 (duas) vias de igual teor e conteúdo, na presença das 02 (duas) testemunhas abaixo arroladas, para que assim produza os efeitos legais esperados.</p><p>Fortaleza-CE {dataatual}</p><br><br><br><p><center>_________________________</center><p style="text-align:center;">Davi Duarte Ribeiro</p><p style="text-align:center;">CONCRETIZA</p><p style="text-align:center;">CNPJ no 30.952.599/0001-24</p><br><p style="text-align:center;">_________________________</p><p style="text-align:center;">{fct.NomeRepresentante}</p><p style="text-align:center;">{fct.CargoRepresentante}</p><p style="text-align:center;">{fct.NomeEmpresa}</p><p style="text-align:center;">{fct.CNPJCliente}</p><p style="text-align:center;">_________________________</p><p style="text-align:center;"><strong>TESTEMUNHA 1:</strong>{fct.Testemunha1}</p><p style="text-align:center;">RG:{fct.RGtestemunha1} </p><p style="text-align:center;">CPF:{fct.CPFTestemunha1}</p><p style="text-align:center;">_________________________</p><p style="text-align:center;"><strong>TESTEMUNHA 2:</strong> {fct.Testemunha2}</p><p style="text-align:center;">RG:{fct.RGtestemunha2}</p><p style="text-align:center;">CPF: {fct.CPFTestemunha2}</p>')
    Contratohtml.close()



    #<p style="text-align:center;">Alinha pro centro </p>
    #<p style="text-align:right;">Alinha pra direita </p> 