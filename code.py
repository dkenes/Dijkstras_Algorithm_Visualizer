import matplotlib.pyplot as plt
import networkx as nx

def PlotGraph(G):
    # Setting the positions of the nodes
    pos = nx.circular_layout(G)
    # Drawing the graph and displaying it
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Function that draws the shortest paths from node 4 to other nodes using Dijkstra's algorithm
# Close the output window to view other shortest paths. Once you close the window, a new window will open.
def PlotShortestPaths(G):
    for j in range(0, 4):
        node = '{}'.format(j)
        # Since some nodes don't have any paths from other nodes and because we will remove node 2, 
        # I added this condition to check before drawing.
        if not (G.has_node(node) and nx.has_path(G, '4', node)):
            continue
        shortest_path = nx.dijkstra_path(G, '4', node)
        # Drawing the edges representing the shortest path
        shortest_path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]

        fig, ax = plt.subplots()

        # Setting the positions of the nodes
        pos = nx.circular_layout(G)

        # Drawing the graph and the shortest path
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, ax=ax, edgelist=shortest_path_edges, edge_color='r', width=3)

        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

        # Drawing the edge weights
        nx.draw_networkx_edge_labels(G, pos=pos, ax=ax, edge_labels=edge_labels)

        # Displaying the plot
        plt.show()

def main():
    # Creating a directed graph
    G = nx.DiGraph()

    # Adding edges to the graph
    G.add_edge('0', '1', weight=5)
    G.add_edge('0', '2', weight=3)
    G.add_edge('0', '4', weight=2)
    G.add_edge('1', '2', weight=2)
    G.add_edge('1', '3', weight=6)
    G.add_edge('2', '1', weight=1)
    G.add_edge('2', '3', weight=2)
    G.add_edge('4', '3', weight=4)
    G.add_edge('4', '2', weight=10)
    G.add_edge('4', '1', weight=6)

    # To see the other graph drawings, close the output window that appears when you run the program. 
    # The next drawing will be displayed.
    PlotGraph(G)
    PlotShortestPaths(G)
    
    # Removing node 2 from the graph
    G.remove_node('2')
    PlotGraph(G)
    PlotShortestPaths(G)

main()
