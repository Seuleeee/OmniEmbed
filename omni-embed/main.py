import streamlit as st
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px


def load_data():
    """
    Placeholder for data loading - replace with your actual data loading method
    """
    # Example: Generate random vectors
    np.random.seed(42)
    vectors = np.random.randn(100, 10)
    return vectors


def visualize_pca(vectors):
    """
    Perform PCA and reduce to 2D for visualization
    """
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(vectors)
    
    df = pd.DataFrame(
        data=pca_result, 
        columns=['PC1', 'PC2']
    )
    
    return df, pca


def main():
    st.title('Vector Visualization with PCA')
    
    # Load vectors
    vectors = load_data()
    
    # Perform PCA
    df_pca, pca = visualize_pca(vectors)
    
    # Plotting
    fig = px.scatter(
        df_pca, 
        x='PC1', 
        y='PC2', 
        title='PCA Visualization of Vectors',
        labels={'PC1': 'First Principal Component', 
                'PC2': 'Second Principal Component'}
    )
    st.plotly_chart(fig)
    
    # Variance explained
    st.subheader('Variance Explained')
    variance_explained = pca.explained_variance_ratio_
    st.write(f"PC1 explains {variance_explained[0]*100:.2f}% of variance")
    st.write(f"PC2 explains {variance_explained[1]*100:.2f}% of variance")
 
main()
