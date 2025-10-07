# Generated from ParserGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserGrammar import ParserGrammar
else:
    from ParserGrammar import ParserGrammar

# This class defines a complete listener for a parse tree produced by ParserGrammar.
class ParserGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ParserGrammar#programa.
    def enterPrograma(self, ctx:ParserGrammar.ProgramaContext):
        pass

    # Exit a parse tree produced by ParserGrammar#programa.
    def exitPrograma(self, ctx:ParserGrammar.ProgramaContext):
        pass


    # Enter a parse tree produced by ParserGrammar#decfuncao.
    def enterDecfuncao(self, ctx:ParserGrammar.DecfuncaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#decfuncao.
    def exitDecfuncao(self, ctx:ParserGrammar.DecfuncaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#tiporetorno.
    def enterTiporetorno(self, ctx:ParserGrammar.TiporetornoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#tiporetorno.
    def exitTiporetorno(self, ctx:ParserGrammar.TiporetornoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#tipo.
    def enterTipo(self, ctx:ParserGrammar.TipoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#tipo.
    def exitTipo(self, ctx:ParserGrammar.TipoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#tipobase.
    def enterTipobase(self, ctx:ParserGrammar.TipobaseContext):
        pass

    # Exit a parse tree produced by ParserGrammar#tipobase.
    def exitTipobase(self, ctx:ParserGrammar.TipobaseContext):
        pass


    # Enter a parse tree produced by ParserGrammar#dimensao.
    def enterDimensao(self, ctx:ParserGrammar.DimensaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#dimensao.
    def exitDimensao(self, ctx:ParserGrammar.DimensaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#parametros.
    def enterParametros(self, ctx:ParserGrammar.ParametrosContext):
        pass

    # Exit a parse tree produced by ParserGrammar#parametros.
    def exitParametros(self, ctx:ParserGrammar.ParametrosContext):
        pass


    # Enter a parse tree produced by ParserGrammar#principal.
    def enterPrincipal(self, ctx:ParserGrammar.PrincipalContext):
        pass

    # Exit a parse tree produced by ParserGrammar#principal.
    def exitPrincipal(self, ctx:ParserGrammar.PrincipalContext):
        pass


    # Enter a parse tree produced by ParserGrammar#bloco.
    def enterBloco(self, ctx:ParserGrammar.BlocoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#bloco.
    def exitBloco(self, ctx:ParserGrammar.BlocoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#decvariavel.
    def enterDecvariavel(self, ctx:ParserGrammar.DecvariavelContext):
        pass

    # Exit a parse tree produced by ParserGrammar#decvariavel.
    def exitDecvariavel(self, ctx:ParserGrammar.DecvariavelContext):
        pass


    # Enter a parse tree produced by ParserGrammar#comando.
    def enterComando(self, ctx:ParserGrammar.ComandoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#comando.
    def exitComando(self, ctx:ParserGrammar.ComandoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#ComandoLinhaLeitura.
    def enterComandoLinhaLeitura(self, ctx:ParserGrammar.ComandoLinhaLeituraContext):
        pass

    # Exit a parse tree produced by ParserGrammar#ComandoLinhaLeitura.
    def exitComandoLinhaLeitura(self, ctx:ParserGrammar.ComandoLinhaLeituraContext):
        pass


    # Enter a parse tree produced by ParserGrammar#ComandoLinhaEscritaLn.
    def enterComandoLinhaEscritaLn(self, ctx:ParserGrammar.ComandoLinhaEscritaLnContext):
        pass

    # Exit a parse tree produced by ParserGrammar#ComandoLinhaEscritaLn.
    def exitComandoLinhaEscritaLn(self, ctx:ParserGrammar.ComandoLinhaEscritaLnContext):
        pass


    # Enter a parse tree produced by ParserGrammar#ComandoLinhaEscrita.
    def enterComandoLinhaEscrita(self, ctx:ParserGrammar.ComandoLinhaEscritaContext):
        pass

    # Exit a parse tree produced by ParserGrammar#ComandoLinhaEscrita.
    def exitComandoLinhaEscrita(self, ctx:ParserGrammar.ComandoLinhaEscritaContext):
        pass


    # Enter a parse tree produced by ParserGrammar#ComandoLinhaAtribuicao.
    def enterComandoLinhaAtribuicao(self, ctx:ParserGrammar.ComandoLinhaAtribuicaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#ComandoLinhaAtribuicao.
    def exitComandoLinhaAtribuicao(self, ctx:ParserGrammar.ComandoLinhaAtribuicaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#ComandoLinhaFuncao.
    def enterComandoLinhaFuncao(self, ctx:ParserGrammar.ComandoLinhaFuncaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#ComandoLinhaFuncao.
    def exitComandoLinhaFuncao(self, ctx:ParserGrammar.ComandoLinhaFuncaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#ComandoLinhaRetorno.
    def enterComandoLinhaRetorno(self, ctx:ParserGrammar.ComandoLinhaRetornoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#ComandoLinhaRetorno.
    def exitComandoLinhaRetorno(self, ctx:ParserGrammar.ComandoLinhaRetornoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#comando_bloco.
    def enterComando_bloco(self, ctx:ParserGrammar.Comando_blocoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#comando_bloco.
    def exitComando_bloco(self, ctx:ParserGrammar.Comando_blocoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#leitura.
    def enterLeitura(self, ctx:ParserGrammar.LeituraContext):
        pass

    # Exit a parse tree produced by ParserGrammar#leitura.
    def exitLeitura(self, ctx:ParserGrammar.LeituraContext):
        pass


    # Enter a parse tree produced by ParserGrammar#dimensao2.
    def enterDimensao2(self, ctx:ParserGrammar.Dimensao2Context):
        pass

    # Exit a parse tree produced by ParserGrammar#dimensao2.
    def exitDimensao2(self, ctx:ParserGrammar.Dimensao2Context):
        pass


    # Enter a parse tree produced by ParserGrammar#escrita.
    def enterEscrita(self, ctx:ParserGrammar.EscritaContext):
        pass

    # Exit a parse tree produced by ParserGrammar#escrita.
    def exitEscrita(self, ctx:ParserGrammar.EscritaContext):
        pass


    # Enter a parse tree produced by ParserGrammar#escritaln.
    def enterEscritaln(self, ctx:ParserGrammar.EscritalnContext):
        pass

    # Exit a parse tree produced by ParserGrammar#escritaln.
    def exitEscritaln(self, ctx:ParserGrammar.EscritalnContext):
        pass


    # Enter a parse tree produced by ParserGrammar#TermoEscritaTexto.
    def enterTermoEscritaTexto(self, ctx:ParserGrammar.TermoEscritaTextoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#TermoEscritaTexto.
    def exitTermoEscritaTexto(self, ctx:ParserGrammar.TermoEscritaTextoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#TermoEscritaExpressao.
    def enterTermoEscritaExpressao(self, ctx:ParserGrammar.TermoEscritaExpressaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#TermoEscritaExpressao.
    def exitTermoEscritaExpressao(self, ctx:ParserGrammar.TermoEscritaExpressaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#selecao.
    def enterSelecao(self, ctx:ParserGrammar.SelecaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#selecao.
    def exitSelecao(self, ctx:ParserGrammar.SelecaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#senao.
    def enterSenao(self, ctx:ParserGrammar.SenaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#senao.
    def exitSenao(self, ctx:ParserGrammar.SenaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#enquanto.
    def enterEnquanto(self, ctx:ParserGrammar.EnquantoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#enquanto.
    def exitEnquanto(self, ctx:ParserGrammar.EnquantoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#para.
    def enterPara(self, ctx:ParserGrammar.ParaContext):
        pass

    # Exit a parse tree produced by ParserGrammar#para.
    def exitPara(self, ctx:ParserGrammar.ParaContext):
        pass


    # Enter a parse tree produced by ParserGrammar#atribuicao.
    def enterAtribuicao(self, ctx:ParserGrammar.AtribuicaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#atribuicao.
    def exitAtribuicao(self, ctx:ParserGrammar.AtribuicaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#para_atribuicoes.
    def enterPara_atribuicoes(self, ctx:ParserGrammar.Para_atribuicoesContext):
        pass

    # Exit a parse tree produced by ParserGrammar#para_atribuicoes.
    def exitPara_atribuicoes(self, ctx:ParserGrammar.Para_atribuicoesContext):
        pass


    # Enter a parse tree produced by ParserGrammar#complemento.
    def enterComplemento(self, ctx:ParserGrammar.ComplementoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#complemento.
    def exitComplemento(self, ctx:ParserGrammar.ComplementoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#funcao.
    def enterFuncao(self, ctx:ParserGrammar.FuncaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#funcao.
    def exitFuncao(self, ctx:ParserGrammar.FuncaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#argumentos.
    def enterArgumentos(self, ctx:ParserGrammar.ArgumentosContext):
        pass

    # Exit a parse tree produced by ParserGrammar#argumentos.
    def exitArgumentos(self, ctx:ParserGrammar.ArgumentosContext):
        pass


    # Enter a parse tree produced by ParserGrammar#retorno.
    def enterRetorno(self, ctx:ParserGrammar.RetornoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#retorno.
    def exitRetorno(self, ctx:ParserGrammar.RetornoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#expressao.
    def enterExpressao(self, ctx:ParserGrammar.ExpressaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#expressao.
    def exitExpressao(self, ctx:ParserGrammar.ExpressaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#expr_ou.
    def enterExpr_ou(self, ctx:ParserGrammar.Expr_ouContext):
        pass

    # Exit a parse tree produced by ParserGrammar#expr_ou.
    def exitExpr_ou(self, ctx:ParserGrammar.Expr_ouContext):
        pass


    # Enter a parse tree produced by ParserGrammar#expr_e.
    def enterExpr_e(self, ctx:ParserGrammar.Expr_eContext):
        pass

    # Exit a parse tree produced by ParserGrammar#expr_e.
    def exitExpr_e(self, ctx:ParserGrammar.Expr_eContext):
        pass


    # Enter a parse tree produced by ParserGrammar#expr_relacional.
    def enterExpr_relacional(self, ctx:ParserGrammar.Expr_relacionalContext):
        pass

    # Exit a parse tree produced by ParserGrammar#expr_relacional.
    def exitExpr_relacional(self, ctx:ParserGrammar.Expr_relacionalContext):
        pass


    # Enter a parse tree produced by ParserGrammar#op_relacional.
    def enterOp_relacional(self, ctx:ParserGrammar.Op_relacionalContext):
        pass

    # Exit a parse tree produced by ParserGrammar#op_relacional.
    def exitOp_relacional(self, ctx:ParserGrammar.Op_relacionalContext):
        pass


    # Enter a parse tree produced by ParserGrammar#expr_aditiva.
    def enterExpr_aditiva(self, ctx:ParserGrammar.Expr_aditivaContext):
        pass

    # Exit a parse tree produced by ParserGrammar#expr_aditiva.
    def exitExpr_aditiva(self, ctx:ParserGrammar.Expr_aditivaContext):
        pass


    # Enter a parse tree produced by ParserGrammar#op_aditivo.
    def enterOp_aditivo(self, ctx:ParserGrammar.Op_aditivoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#op_aditivo.
    def exitOp_aditivo(self, ctx:ParserGrammar.Op_aditivoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#expr_multiplicativa.
    def enterExpr_multiplicativa(self, ctx:ParserGrammar.Expr_multiplicativaContext):
        pass

    # Exit a parse tree produced by ParserGrammar#expr_multiplicativa.
    def exitExpr_multiplicativa(self, ctx:ParserGrammar.Expr_multiplicativaContext):
        pass


    # Enter a parse tree produced by ParserGrammar#op_multiplicativo.
    def enterOp_multiplicativo(self, ctx:ParserGrammar.Op_multiplicativoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#op_multiplicativo.
    def exitOp_multiplicativo(self, ctx:ParserGrammar.Op_multiplicativoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#FatorTermo.
    def enterFatorTermo(self, ctx:ParserGrammar.FatorTermoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#FatorTermo.
    def exitFatorTermo(self, ctx:ParserGrammar.FatorTermoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#FatorText.
    def enterFatorText(self, ctx:ParserGrammar.FatorTextContext):
        pass

    # Exit a parse tree produced by ParserGrammar#FatorText.
    def exitFatorText(self, ctx:ParserGrammar.FatorTextContext):
        pass


    # Enter a parse tree produced by ParserGrammar#FatorNegacaoFator.
    def enterFatorNegacaoFator(self, ctx:ParserGrammar.FatorNegacaoFatorContext):
        pass

    # Exit a parse tree produced by ParserGrammar#FatorNegacaoFator.
    def exitFatorNegacaoFator(self, ctx:ParserGrammar.FatorNegacaoFatorContext):
        pass


    # Enter a parse tree produced by ParserGrammar#FatorExpressao.
    def enterFatorExpressao(self, ctx:ParserGrammar.FatorExpressaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#FatorExpressao.
    def exitFatorExpressao(self, ctx:ParserGrammar.FatorExpressaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#TermoVariavel.
    def enterTermoVariavel(self, ctx:ParserGrammar.TermoVariavelContext):
        pass

    # Exit a parse tree produced by ParserGrammar#TermoVariavel.
    def exitTermoVariavel(self, ctx:ParserGrammar.TermoVariavelContext):
        pass


    # Enter a parse tree produced by ParserGrammar#TermoConstante.
    def enterTermoConstante(self, ctx:ParserGrammar.TermoConstanteContext):
        pass

    # Exit a parse tree produced by ParserGrammar#TermoConstante.
    def exitTermoConstante(self, ctx:ParserGrammar.TermoConstanteContext):
        pass


    # Enter a parse tree produced by ParserGrammar#TermoFuncao.
    def enterTermoFuncao(self, ctx:ParserGrammar.TermoFuncaoContext):
        pass

    # Exit a parse tree produced by ParserGrammar#TermoFuncao.
    def exitTermoFuncao(self, ctx:ParserGrammar.TermoFuncaoContext):
        pass


    # Enter a parse tree produced by ParserGrammar#sinal.
    def enterSinal(self, ctx:ParserGrammar.SinalContext):
        pass

    # Exit a parse tree produced by ParserGrammar#sinal.
    def exitSinal(self, ctx:ParserGrammar.SinalContext):
        pass


    # Enter a parse tree produced by ParserGrammar#constante.
    def enterConstante(self, ctx:ParserGrammar.ConstanteContext):
        pass

    # Exit a parse tree produced by ParserGrammar#constante.
    def exitConstante(self, ctx:ParserGrammar.ConstanteContext):
        pass


    # Enter a parse tree produced by ParserGrammar#AcessoId.
    def enterAcessoId(self, ctx:ParserGrammar.AcessoIdContext):
        pass

    # Exit a parse tree produced by ParserGrammar#AcessoId.
    def exitAcessoId(self, ctx:ParserGrammar.AcessoIdContext):
        pass


    # Enter a parse tree produced by ParserGrammar#AcessoIdArray.
    def enterAcessoIdArray(self, ctx:ParserGrammar.AcessoIdArrayContext):
        pass

    # Exit a parse tree produced by ParserGrammar#AcessoIdArray.
    def exitAcessoIdArray(self, ctx:ParserGrammar.AcessoIdArrayContext):
        pass



del ParserGrammar