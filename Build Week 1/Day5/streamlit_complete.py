import pandas as pd
from pandas.io.parsers import read_csv
import streamlit as st
from PIL import Image
import plotly.express as ex
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


home = st.container()
visualisation = st.container()
about = st.container()
image = Image.open('books.jpeg')
logo_im = Image.open('LOGO.jpeg')

#### file reader, with st.cache, it makes data loading faster
@st.cache
def read_file(filename):
    df = pd.read_csv(filename,dtype=object)
    return df

####################### N a v b a r#################################
logo = st.sidebar.image(logo_im,width=100)

#dropdown menu as a navbar
selected = st.sidebar.selectbox('Navigation'
,('Home','Data Visualization','About'))

#######################################################################
###################     H o m e   P a g e      ########################
#######################################################################
if selected == 'Home':
    with home:
        st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">',unsafe_allow_html=True)
        st.markdown("""
                    <button type="button" class="btn btn-primary position-relative">
                        Home Page
                        <span class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </button>
                """,unsafe_allow_html=True)
        st.write('\n'*10)
        st.subheader('The Best Epic Fantasy (fiction) - books collection')
        st.image(image,'Best epic fantasy books')
        


#######################################################################
####################### Data Visualisation page #######################
#######################################################################

elif selected == 'Data Visualization':
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">',unsafe_allow_html=True)
    st.markdown("""
                    <button type="button" class="btn btn-primary position-relative">
                        Data Visualization Page
                        <span class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </button>
                """,unsafe_allow_html=True)

####################### showing the list of books #####################
    file1 = 'full_with_awards_count.csv'
    df = read_file(file1).drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)
    
    
    #trigger checkbox to show or not to show the list of books
    show_books = st.sidebar.checkbox('show the list of books') 
    if show_books:
        # user inputs the number of books using slider
        how_many_books = st.sidebar.slider('how many books to show',min_value=0,max_value=3600,step=5)
        st.sidebar.markdown("""<hr>""",unsafe_allow_html=True)
        filter_opt = df.columns
        filters = st.sidebar.multiselect('what do you want to show',filter_opt)
        if how_many_books:
            fig = go.Figure(data=[go.Table(
                header = dict(values = filters,
                        fill_color='paleturquoise',
                        align = 'left'),
                cells=dict(values = [df[i].head(how_many_books) for i in df[filters].columns],
                        fill_color='lavender',
                        align='left'
            )
        )])
            st.write(fig)

######################## data for charts #################################

    df1 = read_csv('data.csv')
    show_graphs = st.sidebar.checkbox('show graphs')

    if show_graphs:
        pie_1 = 'Share of books according to their size(pie chart)'
        pie_2 = 'Share of books according to their rating(pie chart)'
        scatter_1 ='Pages-reviews relationship'
        scatter_2 = 'Ratings-reviews replationship'
        bar_1 = 'Books with most awards'
        bar_2 = 'Number of books published per year'
        bar_3   = 'Authors with most awards'
        bar_4 = 'single/book series'
        bar_5 = 'Number of books published by authors'
        d3_1 = 'Book size-rating-reviews relationship(3D scatter graph)'
        d3_2 = 'Awards-rating-reviews relationship(3D scatter graph)'
        heat_1 = 'Correlation between book parameters'
        heat_2 = 'Pair-plot(Correlations)'
        graph_opt = [pie_1, pie_2,scatter_1,scatter_2,bar_1,bar_2,bar_3,bar_4,bar_5,d3_1,d3_2,heat_1,heat_2]
        figure_type = st.sidebar.multiselect('choose type of graph:',graph_opt)
        
        
        
    ######################### scatter charts #############################
        if scatter_1 in figure_type:
            fig_scatter_1 = ex.scatter(df1,x='num_pages', y='Reviews',color="Rating",
            labels={'num_pages':'number of pages',
            'Reviews':'Number of reviews(normalized)',
            "Rating":'Rating range'})
            fig_scatter_1.update_layout(
            title={
                'text': "Reviews based on the length of the book",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
            st.write(fig_scatter_1)
            st.markdown("""<hr>""",unsafe_allow_html=True)
        
        if scatter_2 in figure_type:
            fig_scatter_2 = ex.scatter(df1,x='Average_rating', y='Reviews',color="Rating",labels={'num_pages':'Number of pages',
            'Average_rating':'Average of rating(normalized)',
            "Rating":'Rating range'})
            fig_scatter_2.update_layout(
            title={
                'text': "Reviews based on the Average rating",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
            
            st.write(fig_scatter_2)
            st.markdown("""<hr>""",unsafe_allow_html=True)

        

        ######################### pie charts #################################

        fig_pie_1 = ex.pie(df1, values='num_pages', names='Pages_class', title='shares of books according to their size',color_discrete_sequence=ex.colors.sequential.RdBu)
        fig_pie_1.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie_1.update_layout(title_x=0.48)
        if pie_1 in figure_type:
            st.write(fig_pie_1)
            st.markdown("""<hr>""",unsafe_allow_html=True)
        

        fig_pie_2 = ex.pie(df1, values='Average_rating', names='Rating', title='shares of books according to their ratings',color_discrete_sequence=ex.colors.sequential.RdBu_r)
        fig_pie_2.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie_2.update_layout(title_x=0.47)
        if pie_2 in figure_type:
            st.write(fig_pie_2)
            st.markdown("""<hr>""",unsafe_allow_html=True)

        ######################### bar charts ###############################
        if bar_1 in figure_type:
            how_many = st.sidebar.slider('choose the number of books to show:',min_value=1,max_value=100,value=10)
            st.sidebar.markdown("""<hr>""",unsafe_allow_html=True)
            df2=df1.pivot_table(index='title',values='awards_count',aggfunc='sum').sort_values('awards_count',ascending=False).head(how_many)
            bar_fig_1 = ex.bar(df2,x=df2.index,y="awards_count",category_orders=dict(a="awards_count"),color_discrete_sequence=ex.colors.sequential.Inferno,
            labels={'num_pages':'Number of pages',
            'Average_rating':'Average of rating(normalized)',
            "Rating":'Rating range',
            "title":"Movie names",
            "awards_count":"Number of awards received"},title='Books with most awards',width=800,height=600)
            bar_fig_1.update_layout(bargap=0.2)
            bar_fig_1.update_layout(
            title={
                'text': "Number of awards won by book",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
            st.write(bar_fig_1)
            st.markdown("""<hr>""",unsafe_allow_html=True)
        

        if bar_2 in figure_type:
            inter = st.sidebar.slider('choose interval for years',value=[0,2022])
            st.sidebar.markdown("""<hr>""",unsafe_allow_html=True)
            df2=df1[df1['publish_year']>inter[0]]
            df2= df2[df2['publish_year']<inter[1]]
            df2['Book_count'] = 1
            try:
                df3 = df2.pivot_table(index='publish_year',values='Book_count',aggfunc='sum').sort_values('Book_count',ascending=False)
                bar_fig_2 = ex.bar(df3,x=df3.index,y="Book_count",category_orders=dict(a="Book_count"),
                labels={'num_pages':'Number of pages',
                        'Average_rating':'Average of rating(normalized)',
                        "Rating":'Rating range',
                        "title":"Movie names",
                        "awards_count":"Number of awards received",
                        "author":"Author names",
                        "Book_count":"Number of Books",
                        "publish_year":"Original year of publications"})
                bar_fig_2.update_layout(
                title={
                    'text': "Number of books published by year",
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})
                bar_fig_2.update_layout(bargap=0.2)
                st.write(bar_fig_2)
                st.markdown("""<hr>""",unsafe_allow_html=True)
            except:
                st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">""",unsafe_allow_html=True)

                st.markdown("""
                <div class="alert alert-warning" role="alert">
                There is no any book in chosen interval, expand your interval !
                </div>
                """,unsafe_allow_html=True)
                st.markdown("""<hr>""",unsafe_allow_html=True)


        if bar_3 in figure_type:
            how_many_2= st.sidebar.slider('choose the number of authors to show:',min_value=1,max_value=100,value=10)
            st.sidebar.markdown("""<hr>""",unsafe_allow_html=True)
            df4=df1.pivot_table(index='author',values='awards_count',aggfunc='sum').sort_values('awards_count',ascending=False).head(how_many_2)
            bar_fig_3 = ex.bar(df4,x=df4.index,y="awards_count",category_orders=dict(a="awards_count"),color_discrete_sequence=ex.colors.sequential.Cividis,
            labels={'num_pages':'Number of pages',
                        'Average_rating':'Average of rating(normalized)',
                        "Rating":'Rating range',
                        "title":"Movie names",
                        "awards_count":"Number of awards received",
                        "author":"Author names"})
            bar_fig_3.update_layout(
            title={
                'text': "Number of awards won by author",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
            bar_fig_3.update_layout(bargap=0.2)
            st.write(bar_fig_3)
            st.markdown("""<hr>""",unsafe_allow_html=True)

        if bar_4 in figure_type:
            bar_fig_4 = plt.figure(figsize=(13,6))
            ax = sns.countplot(x="series_bol", hue="series_bol", data=df1,palette="Set1")
            ax.set_title('Book has series or not', size=15)
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
            ax.set(xlabel='series', ylabel='Number of books')
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 15})
            for p in ax.patches:
                    ax.annotate(p.get_height(), (p.get_x()+0.1, p.get_height()+50))
            plt.legend(loc='upper left', labels=['Single book', 'Part of book series'])
            st.write(bar_fig_4)
            st.markdown("""<hr>""",unsafe_allow_html=True)

        if bar_5 in figure_type:
            bar_fig_5 = plt.figure(figsize=(12,6))
            top_author=df1['author'].value_counts()[:20]
            sns.barplot(top_author.values, top_author.index, palette='terrain').set_title('Number of Books Published by the Authors')
            plt.xlabel("Number of Books")
            plt.ylabel("Name of the Authors")
            st.write(bar_fig_5)
            st.markdown("""<hr>""",unsafe_allow_html=True)
    ######################### 3D graphs ##################################
        if d3_1 in figure_type:
            d3_fig_1 = ex.scatter_3d(df1,x="Reviews",y="Average_rating",z="Pages_class",color="Pages_class",opacity=0.5,
            labels={'num_pages':'Number of pages',
            'Average_rating':'Average of rating(normalized)',
            "Rating":'Rating range',
            "title":"Movie names",
            "awards_count":"Number of awards received",
            "author":"Author names",
            "Book_count":"Number of Books",
            "publish_year":"Original year of publications",
            "Pages_class":"Book type"})
            d3_fig_1.update_layout(
            title={
                'text': "3D plot to compare Average rating and Reviews based on Book length",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
            st.write(d3_fig_1)
            st.markdown("""<hr>""",unsafe_allow_html=True)

        if d3_2 in figure_type:
            d3_fig_2 = ex.line_3d(df1,x="Reviews",y="Average_rating",z="awards_count",color="Pages_class",
            labels={'num_pages':'Number of pages',
            'Average_rating':'Average of rating(normalized)',
            "Rating":'Rating range',
            "title":"Movie names",
            "awards_count":"Number of awards received",
            "author":"Author names",
            "Book_count":"Number of Books",
            "publish_year":"Original year of publications",
            "Pages_class":"Book type"})
            d3_fig_2.update_layout(
            title={
                'text': "3D plot to compare Average rating and Reviews based on Number of awards received",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
            st.write(d3_fig_2)
            st.markdown("""<hr>""",unsafe_allow_html=True)
    ######################### heatmaps ###################################
        if heat_1 in figure_type:
            df_heat = df1[["title","author","Reviews","Total_ratings","Average_rating","num_pages","publish_year","series","awards_count",'Rating']]
            heat_fig = plt.figure(figsize=(6,6))
            sns.heatmap(df_heat.corr(),annot=True,cmap="RdGy").set(title='Correlation between book parameters')
            st.write(heat_fig)
            
            st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">""",unsafe_allow_html=True)

            st.markdown("""
               <div class="alert alert-primary d-flex align-items-center" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                </svg>
                <div>
                    An example alert with an icon
                </div>
                </div>
            """,unsafe_allow_html=True)
            st.markdown("""<hr>""",unsafe_allow_html=True)
        
        # if heat_2 in figure_type:
        #     df_heat2 = df1[["title","author","Reviews","Total_ratings","Average_rating","num_pages","publish_year","series","awards_count",'Rating']]
        #     df10_pairplot = df_heat2.dropna()
        #     pair_plot=sns.pairplot(df10_pairplot,height=1.5,hue="Rating")

        #     st.write(pair_plot)
        #     st.markdown("""<hr>""",unsafe_allow_html=True)

    ######################## instruction how to use ######################
    if not show_graphs and not show_books:
        st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">""",unsafe_allow_html=True)

        st.markdown("""
                <div class="alert alert-primary" role="alert">
                <h4>instruction for effective usage</h4>
                <h6 it's possible to choose what to display in this section</h6>
                <p>choose either or both checkboxes in the sidebar, to display particular type of visualization</p>
                <hr>
                <p class="mb-0"></p>
                </div>
            """,unsafe_allow_html=True)

    
        
    if show_books and not show_graphs and not how_many_books and not filters:
            st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">""",unsafe_allow_html=True)

            st.markdown("""
                <div class="alert alert-primary" role="alert">
                <h4 class="alert-heading">Table parameters</h4>
                <h5 class="alert-heading">There are some parameters to render the table:</h5>
                <hr>
                <p>-specify number of books to dislay using slider which is in the sidebar</p>
                <p>-specify one or multiple parameter of the book, using dropdown menu in the sidebar</p>
                <hr>
                <p class="mb-0"></p>
                </div>
            """,unsafe_allow_html=True)
    if not show_books and show_graphs and not figure_type :
            st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">""",unsafe_allow_html=True)

            st.markdown("""
                <div class="alert alert-primary" role="alert">
                <h4 class="alert-heading">Graphs parameters</h4>
                <h5 class="alert-heading">There are some parameters to render the graphs:</h5>
                <p>it's possible to choose one or multiple relationship graphs from dropdown menu in the sidebar</p>
                <hr>
                </div>
            """,unsafe_allow_html=True)
            


    ######################################################################
    ##################      About Page        ############################
    ######################################################################
elif selected == 'About':
    team = st.container()
    tools = st.container()
    with about:
        st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">',unsafe_allow_html=True)
        st.markdown("""
                    <button type="button" class="btn btn-primary position-relative">
                        About Page
                        <span class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </button>
                """,unsafe_allow_html=True)

        with team:
           st.subheader('Team')
           st.markdown("""
            ** Saidalikhon **- Data scraping / streamlit \n
            ** Sai **- Data visualization \n
            ** Sohan **- preprocessing \n
            ** Irene **- preprocessing \n
           """)
        with tools:
            st.subheader('Tools')
            st.markdown("""
                ** Streamlit **- creation of data app \n
                ** Plotly **- plotting / visualization \n
                ** Selenium **- data scraping  \n
                ** Pandas **- Data processing/analysis \n
            """)

        



