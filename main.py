import streamlit as st
import Preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = Preprocessor.preprocess(data)



    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox("Show User Analysis", user_list)

    if st.sidebar.button('Show Analysis'):
        st.title("Top Statistic")
        num_messages, words, num_media, links = helper.fetch_stat(selected_user, df)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total words")
            st.title(words)

        with col3:
            st.header("Number Of Media Messages")
            st.title(num_media)

        with col4:
            st.header("Number of links Shares")
            st.title(links)


        #
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)


            with col1:
                ax.bar(x.index, x.values, color='orange')
                plt.xticks(rotation = 45)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:

            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:

            st.header("Most Busy Month")
            busy_month = helper.montly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='red')
            plt.xticks(rotation=45)
            st.pyplot(fig)


        st.title('WordCloud')
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)




        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation=90)
        st.title('Most Common Words')
        st.pyplot(fig)

        st.dataframe(most_common_df)


        emoji_df = helper.emojis_helper(selected_user,df)
        st.title("Emoji Analysis")

        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(), autopct='%0.2f')
            st.pyplot(fig)


        timeline = helper.montly_timeline(selected_user,df)
        st.title("Montly Timeline")
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'])
        plt.xticks(rotation=45)
        st.pyplot(fig)


        daily_timeline = helper.daily_timeline(selected_user, df)
        st.title("Daily Timeline")
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['exact_date'], daily_timeline['message'], color = 'red')
        plt.xticks(rotation=45)
        st.pyplot(fig)



        st.title("Weekly Activity Heatmap")
        user_heatmap = helper.activity_map_heatmap(selected_user,df)
        st.title("Daily Timeline")
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        plt.yticks(rotation=45)
        st.pyplot(fig)