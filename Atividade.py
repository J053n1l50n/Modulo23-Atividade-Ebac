from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd



def c_g(df):
    # Gráfico 1: Histograma da distribuição de preços
    fig1 = px.histogram(df, x='Preço', nbins=20, title='Distribuição de Preços')


    core = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod', 'Nota_MinMax', 'N_Avaliações_MinMax',
               'Desconto_MinMax', 'Preço_MinMax', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Marca_Freq',
               'Material_Freq']].corr()


    fig2 = px.imshow(core, text_auto=True)
    fig2.update_layout(title="Mapa de Calor da Correlação entre Variáveis")


    fig3 = px.scatter(df, x='Preço', y='Preço_MinMax')
    fig3.update_layout(
        title='Dispersão do Preço',
        xaxis_title='Preço',
        yaxis_title='Preço',

    )

    # Gráfico 4: Gráfico de pizza da porcentagem de temporadas
    fig4 = px.pie(df, names='Temporada', color='Temporada')
    fig4.update_layout(
        title='Porcentagem de Temporadas'
    )

    # Gráfico 5: Gráfico de barras da quantidade de temporadas
    fig5 = px.bar(df, x='Temporada', y='Temporada', orientation='h')
    fig5.update_layout(
        title="Quantidade de Temporadas",
        xaxis_title="Quantidade",
        yaxis_title="Temporadas",

    )

    fig6 = px.histogram(df, x='Nota', y='Nota')
    fig6.update_layout(title="Densidade de Notas",
                       xaxis_title="Notas",
                       yaxis_title="Quantidade",
                       )


    fig7 = px.scatter(df, x='N_Avaliações', y='N_Avaliações_MinMax')
    fig7.update_layout(
        title="Regressão entre N° de Avaliações e sua Padronização",
        xaxis_title="N° de Avaliações",
        yaxis_title="Padronização",

    )
    return fig1, fig2, fig3, fig4, fig5, fig6, fig7


def cria_app(df):
        app = Dash(__name__)
        # Chama a função c_g para obter todas as figuras
        fig1, fig2, fig3, fig4, fig5, fig6, fig7 = c_g(df)

        # Define o layout do aplicativo com todos os gráficos
        app.layout = html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2),
            dcc.Graph(figure=fig3),
            dcc.Graph(figure=fig4),
            dcc.Graph(figure=fig5),
            dcc.Graph(figure=fig6),
            dcc.Graph(figure=fig7)
        ])
        return app


df=pd.read_csv('ecommerce_estatistica.csv')

if __name__ == '__main__':
    app= cria_app(df)

    app.run(debug=True, port=8050)