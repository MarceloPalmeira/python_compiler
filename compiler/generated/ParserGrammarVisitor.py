# Generated from ParserGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserGrammar import ParserGrammar
else:
    from ParserGrammar import ParserGrammar

# This class defines a complete generic visitor for a parse tree produced by ParserGrammar.

class ParserGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserGrammar#programa.
    def visitPrograma(self, ctx:ParserGrammar.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#decfuncao.
    def visitDecfuncao(self, ctx:ParserGrammar.DecfuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#tiporetorno.
    def visitTiporetorno(self, ctx:ParserGrammar.TiporetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#tipo.
    def visitTipo(self, ctx:ParserGrammar.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#tipobase.
    def visitTipobase(self, ctx:ParserGrammar.TipobaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#dimensao.
    def visitDimensao(self, ctx:ParserGrammar.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#parametros.
    def visitParametros(self, ctx:ParserGrammar.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#principal.
    def visitPrincipal(self, ctx:ParserGrammar.PrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#bloco.
    def visitBloco(self, ctx:ParserGrammar.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#decvariavel.
    def visitDecvariavel(self, ctx:ParserGrammar.DecvariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#comando.
    def visitComando(self, ctx:ParserGrammar.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#ComandoLinhaLeitura.
    def visitComandoLinhaLeitura(self, ctx:ParserGrammar.ComandoLinhaLeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#ComandoLinhaEscritaLn.
    def visitComandoLinhaEscritaLn(self, ctx:ParserGrammar.ComandoLinhaEscritaLnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#ComandoLinhaEscrita.
    def visitComandoLinhaEscrita(self, ctx:ParserGrammar.ComandoLinhaEscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#ComandoLinhaAtribuicao.
    def visitComandoLinhaAtribuicao(self, ctx:ParserGrammar.ComandoLinhaAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#ComandoLinhaFuncao.
    def visitComandoLinhaFuncao(self, ctx:ParserGrammar.ComandoLinhaFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#ComandoLinhaRetorno.
    def visitComandoLinhaRetorno(self, ctx:ParserGrammar.ComandoLinhaRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#comando_bloco.
    def visitComando_bloco(self, ctx:ParserGrammar.Comando_blocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#leitura.
    def visitLeitura(self, ctx:ParserGrammar.LeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#dimensao2.
    def visitDimensao2(self, ctx:ParserGrammar.Dimensao2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#escrita.
    def visitEscrita(self, ctx:ParserGrammar.EscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#escritaln.
    def visitEscritaln(self, ctx:ParserGrammar.EscritalnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#TermoEscritaTexto.
    def visitTermoEscritaTexto(self, ctx:ParserGrammar.TermoEscritaTextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#TermoEscritaExpressao.
    def visitTermoEscritaExpressao(self, ctx:ParserGrammar.TermoEscritaExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#selecao.
    def visitSelecao(self, ctx:ParserGrammar.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#senao.
    def visitSenao(self, ctx:ParserGrammar.SenaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#enquanto.
    def visitEnquanto(self, ctx:ParserGrammar.EnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#para.
    def visitPara(self, ctx:ParserGrammar.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#atribuicao.
    def visitAtribuicao(self, ctx:ParserGrammar.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#para_atribuicoes.
    def visitPara_atribuicoes(self, ctx:ParserGrammar.Para_atribuicoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#complemento.
    def visitComplemento(self, ctx:ParserGrammar.ComplementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#funcao.
    def visitFuncao(self, ctx:ParserGrammar.FuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#argumentos.
    def visitArgumentos(self, ctx:ParserGrammar.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#retorno.
    def visitRetorno(self, ctx:ParserGrammar.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#expressao.
    def visitExpressao(self, ctx:ParserGrammar.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#expr_ou.
    def visitExpr_ou(self, ctx:ParserGrammar.Expr_ouContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#expr_e.
    def visitExpr_e(self, ctx:ParserGrammar.Expr_eContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#expr_relacional.
    def visitExpr_relacional(self, ctx:ParserGrammar.Expr_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#op_relacional.
    def visitOp_relacional(self, ctx:ParserGrammar.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#expr_aditiva.
    def visitExpr_aditiva(self, ctx:ParserGrammar.Expr_aditivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#op_aditivo.
    def visitOp_aditivo(self, ctx:ParserGrammar.Op_aditivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#expr_multiplicativa.
    def visitExpr_multiplicativa(self, ctx:ParserGrammar.Expr_multiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#op_multiplicativo.
    def visitOp_multiplicativo(self, ctx:ParserGrammar.Op_multiplicativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#FatorTermo.
    def visitFatorTermo(self, ctx:ParserGrammar.FatorTermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#FatorText.
    def visitFatorText(self, ctx:ParserGrammar.FatorTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#FatorNegacaoFator.
    def visitFatorNegacaoFator(self, ctx:ParserGrammar.FatorNegacaoFatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#FatorExpressao.
    def visitFatorExpressao(self, ctx:ParserGrammar.FatorExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#TermoVariavel.
    def visitTermoVariavel(self, ctx:ParserGrammar.TermoVariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#TermoConstante.
    def visitTermoConstante(self, ctx:ParserGrammar.TermoConstanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#TermoFuncao.
    def visitTermoFuncao(self, ctx:ParserGrammar.TermoFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#sinal.
    def visitSinal(self, ctx:ParserGrammar.SinalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#constante.
    def visitConstante(self, ctx:ParserGrammar.ConstanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#AcessoId.
    def visitAcessoId(self, ctx:ParserGrammar.AcessoIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserGrammar#AcessoIdArray.
    def visitAcessoIdArray(self, ctx:ParserGrammar.AcessoIdArrayContext):
        return self.visitChildren(ctx)



del ParserGrammar