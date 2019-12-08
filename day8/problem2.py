def main():
    img_width = 25
    img_height = 6

    with open("input.txt", "r+") as file:
        image_enc = file.readline()

        layers = []
        layer = []
        row = []

        # create all layers
        for i in range(1, image_enc.__len__()+1):
            row.append(image_enc[i-1])
            if i % img_width == 0:
                layer.append(row)
                row = []
            if i % (img_width * img_height) == 0:
                layers.append(layer)
                layer = []

        # create a dict with all coordinates
        image_dict = {}
        for y in range(img_height):
            for x in range(img_width):
                image_dict[(x, y)] = ''

        # initialize decoded image
        image_dec = []
        for y in range(img_height):
            image_dec.append([])
            for x in range(img_width):
                image_dec[y].append('')

        # decode image
        for layer in layers:
            for coordinates in list(image_dict.keys()):
                x = coordinates[0]
                y = coordinates[1]
                if layer[y][x] != '2':
                    image_dec[y][x] = 'X' if layer[y][x] == '1' else '`'
                    image_dict.pop(coordinates)

        # print image: ZYBLH
        for row in image_dec:
            print()
            for pixel in row:
                print(pixel, end=' ')


if __name__ == "__main__":
    main()

