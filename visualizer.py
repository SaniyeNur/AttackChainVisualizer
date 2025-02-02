import json
import matplotlib.pyplot as plt
import networkx as nx

def load_attack_chain(file_path):
    """JSON dosyasını yükler ve saldırı zincirini döndürür."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['attack_chain']

def create_attack_graph(attack_chain):
    """MITRE ATT&CK zincirini görselleştiren bir grafik oluşturur."""
    graph = nx.DiGraph()  # Yönlü bir grafik oluşturuyoruz

    for step in attack_chain:
        node_label = f"{step['step']}: {step['tactic']}\n{step['technique']}"
        graph.add_node(step['step'], label=node_label)
    
    # Adımları bağlayan kenarları ekle
    for i in range(len(attack_chain) - 1):
        graph.add_edge(attack_chain[i]['step'], attack_chain[i + 1]['step'])
    
    return graph

def visualize_attack_graph(graph):
    """Grafiği çizdirir."""
    pos = nx.spring_layout(graph)  # Grafiğin düzenini belirle
    labels = nx.get_node_attributes(graph, 'label')

    # Düğümleri ve etiketlerini çizdir
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)

    plt.title("MITRE ATT&CK Chain Visualization")
    plt.show()

# Kullanım
if __name__ == "__main__":
    attack_chain = load_attack_chain("/Users/nur.cintimur/Downloads/attack_chain2.json")  # Örnek JSON dosyası
    graph = create_attack_graph(attack_chain)
    visualize_attack_graph(graph)
