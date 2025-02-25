import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx
from matplotlib.colors import ListedColormap
import os

# Create directory for saving visualizations
os.makedirs('visualizations', exist_ok=True)

# Load your data
# Assuming your data is in a CSV file named 'genomic_data.csv'
# If it's in a different format, you'll need to adjust this part
df = pd.read_csv('cleaned_antimicrobial_resistance_data.csv')

# Print column names to identify the correct ones
print("Available columns in your dataset:")
print(df.columns.tolist())

# For this example, we'll use 'Source Organism' as the sample identifier
# Replace 'Source Organism' with the actual column that identifies your samples
sample_id_column = 'Source Organism'
gene_column = 'Gene'
antibiotics_column = 'Product'  # Assuming Product corresponds to Antibiotics
antibiotics_class_column = 'Function'  # Assuming Function corresponds to Antibiotics Class
classification_column = 'Classification'

# 1. Gene against Sample ID
plt.figure(figsize=(12, 10))
gene_sample = pd.crosstab(df[sample_id_column], df[gene_column])
sns.heatmap(gene_sample, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{gene_column} against {sample_id_column}', fontsize=16)
plt.ylabel(sample_id_column, fontsize=14)
plt.xlabel(gene_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/1_gene_sample_id.png', dpi=300)
plt.close()

# 2. Antibiotics class against Sample ID
plt.figure(figsize=(12, 10))
antibiotic_class_sample = pd.crosstab(df[sample_id_column], df[antibiotics_class_column])
sns.heatmap(antibiotic_class_sample, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{antibiotics_class_column} against {sample_id_column}', fontsize=16)
plt.ylabel(sample_id_column, fontsize=14)
plt.xlabel(antibiotics_class_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/2_antibiotics_class_sample_id.png', dpi=300)
plt.close()

# 3. Antibiotics against Sample ID
plt.figure(figsize=(14, 10))
antibiotics_sample = pd.crosstab(df[sample_id_column], df[antibiotics_column])
sns.heatmap(antibiotics_sample, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{antibiotics_column} against {sample_id_column}', fontsize=16)
plt.ylabel(sample_id_column, fontsize=14)
plt.xlabel(antibiotics_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/3_antibiotics_sample_id.png', dpi=300)
plt.close()

# 4. Classification against Sample ID
plt.figure(figsize=(12, 10))
classification_sample = pd.crosstab(df[sample_id_column], df[classification_column])
sns.heatmap(classification_sample, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{classification_column} against {sample_id_column}', fontsize=16)
plt.ylabel(sample_id_column, fontsize=14)
plt.xlabel(classification_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/4_classification_sample_id.png', dpi=300)
plt.close()

# 5. Gene against Antibiotic class
plt.figure(figsize=(14, 12))
gene_antibiotic_class = pd.crosstab(df[gene_column], df[antibiotics_class_column])
sns.heatmap(gene_antibiotic_class, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{gene_column} against {antibiotics_class_column}', fontsize=16)
plt.ylabel(gene_column, fontsize=14)
plt.xlabel(antibiotics_class_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/5_gene_antibiotic_class.png', dpi=300)
plt.close()

# 6. Gene against Classification
plt.figure(figsize=(14, 12))
gene_classification = pd.crosstab(df[gene_column], df[classification_column])
sns.heatmap(gene_classification, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{gene_column} against {classification_column}', fontsize=16)
plt.ylabel(gene_column, fontsize=14)
plt.xlabel(classification_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/6_gene_classification.png', dpi=300)
plt.close()

# 7. Antibiotics Class against Classification
plt.figure(figsize=(12, 10))
antibiotic_class_classification = pd.crosstab(df[antibiotics_class_column], df[classification_column])
sns.heatmap(antibiotic_class_classification, cmap='viridis', cbar_kws={'label': 'Count'})
plt.title(f'{antibiotics_class_column} against {classification_column}', fontsize=16)
plt.ylabel(antibiotics_class_column, fontsize=14)
plt.xlabel(classification_column, fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('visualizations/7_antibiotic_class_classification.png', dpi=300)
plt.close()

# Additional: Network visualization showing relationships
plt.figure(figsize=(16, 14))

# Create a graph
G = nx.Graph()

# Add nodes for each unique Gene, Antibiotics, Antibiotics Class, and Classification
for gene in df[gene_column].unique():
    G.add_node(gene, type='Gene')
for antibiotic in df[antibiotics_column].unique():
    G.add_node(antibiotic, type='Antibiotic')
for antibiotic_class in df[antibiotics_class_column].unique():
    G.add_node(antibiotic_class, type='Antibiotic Class')
for classification in df[classification_column].unique():
    G.add_node(classification, type='Classification')

# Add edges between connected entities
for _, row in df.iterrows():
    G.add_edge(row[gene_column], row[antibiotics_column])
    G.add_edge(row[antibiotics_column], row[antibiotics_class_column])
    G.add_edge(row[antibiotics_class_column], row[classification_column])

# Define node colors by type
node_colors = {'Gene': 'red', 'Antibiotic': 'blue', 'Antibiotic Class': 'green', 'Classification': 'purple'}
colors = [node_colors[G.nodes[node]['type']] for node in G.nodes]

# Use a spring layout for the network
pos = nx.spring_layout(G, seed=42, k=0.5)

# Draw the network
nx.draw(G, pos, node_color=colors, with_labels=True, font_size=10, node_size=800, alpha=0.8, 
        font_weight='bold', edge_color='gray', width=1.5)

# Add a legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=key,
                             markerfacecolor=value, markersize=10)
                  for key, value in node_colors.items()]
plt.legend(handles=legend_elements, loc='upper right', fontsize=12)

plt.title('Relationship Network Between Genes, Antibiotics, Classes, and Classifications', fontsize=16)
plt.tight_layout()
plt.savefig('visualizations/8_relationship_network.png', dpi=300, bbox_inches='tight')
plt.close()

# Create chord diagram to show relationships (requires holoviews and bokeh)
# Uncomment if these libraries are available
"""
import holoviews as hv
from holoviews import opts, dim
hv.extension('bokeh')

# Create edges dataframe for chord diagram
edges = []
for _, row in df.iterrows():
    edges.append((row['Gene'], row['Antibiotics']))
    edges.append((row['Antibiotics'], row['Antibiotics_Class']))
    edges.append((row['Antibiotics_Class'], row['Classification']))

edges_df = pd.DataFrame(edges, columns=['source', 'target'])
edges_df['value'] = 1

# Count occurrences of each edge
edge_counts = edges_df.groupby(['source', 'target']).sum().reset_index()

# Create chord diagram
chord = hv.Chord((edge_counts, hv.Dataset(pd.concat([
    pd.DataFrame({'name': df['Gene'].unique(), 'type': 'Gene'}),
    pd.DataFrame({'name': df['Antibiotics'].unique(), 'type': 'Antibiotic'}),
    pd.DataFrame({'name': df['Antibiotics_Class'].unique(), 'type': 'Antibiotic Class'}),
    pd.DataFrame({'name': df['Classification'].unique(), 'type': 'Classification'})
]))))

chord.opts(
    opts.Chord(cmap='Category10', edge_cmap='Category10', edge_color=dim('source').str(),
               labels='name', node_color=dim('type').str(), width=800, height=800)
)

hv.save(chord, 'visualizations/9_chord_diagram.html')
"""

# Additional: Create a bar chart showing count of genes by antibiotic class
plt.figure(figsize=(14, 8))
gene_counts = df.groupby(antibiotics_class_column)[gene_column].nunique().sort_values(ascending=False)
ax = gene_counts.plot(kind='bar', color='teal')
plt.title(f'Number of Unique {gene_column}s per {antibiotics_class_column}', fontsize=16)
plt.xlabel(antibiotics_class_column, fontsize=14)
plt.ylabel(f'Number of Unique {gene_column}s', fontsize=14)
plt.xticks(rotation=90)
# Add count labels on top of bars
for i, v in enumerate(gene_counts):
    ax.text(i, v + 0.1, str(v), ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('visualizations/10_gene_count_by_antibiotic_class.png', dpi=300)
plt.close()

# Additional: Create a bar chart showing count of antibiotics by classification
plt.figure(figsize=(14, 8))
antibiotics_counts = df.groupby(classification_column)[antibiotics_column].nunique().sort_values(ascending=False)
ax = antibiotics_counts.plot(kind='bar', color='orange')
plt.title(f'Number of Unique {antibiotics_column}s per {classification_column}', fontsize=16)
plt.xlabel(classification_column, fontsize=14)
plt.ylabel(f'Number of Unique {antibiotics_column}s', fontsize=14)
plt.xticks(rotation=90)
# Add count labels on top of bars
for i, v in enumerate(antibiotics_counts):
    ax.text(i, v + 0.1, str(v), ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('visualizations/11_antibiotics_count_by_classification.png', dpi=300)
plt.close()

print("All visualizations have been saved to the 'visualizations' directory.")
