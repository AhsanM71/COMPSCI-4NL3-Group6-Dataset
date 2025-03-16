class Loader:
    
    def get_label(self):
        with open("../output/predicted_label", 'r') as f:
            predicted_label = [int(line.strip()) for line in f.readlines()] 
        return predicted_label
    
    
