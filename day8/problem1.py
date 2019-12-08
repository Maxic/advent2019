def main():
    img_width = 25
    img_height = 6

    with open("input.txt", "r+") as file:
        image = file.readline()

        layers = []
        layer = []
        row = []

        for i in range(1, image.__len__()+1):
            layer.append(image[i-1])
            #if i % img_width == 0:
            if i % (img_width * img_height) == 0:
                layers.append(layer)
                layer = []

        layer_digits = {}

        # for all layers, count '0' digits
        for layer in layers:
            layer_digits[layers.index(layer)] = (layer.count('0'), layer.count('1'), layer.count('2'))
            # lowest count was 6, don't feel like writing this out. Part 2 should be more interesting.
            if layer.count('0') == 6:
                print(layer.count('1') * layer.count('2'))


if __name__ == "__main__":
    main()

