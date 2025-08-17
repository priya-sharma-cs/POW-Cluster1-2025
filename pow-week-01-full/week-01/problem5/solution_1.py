def flood_fill(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0]) if image else 0
    if rows == 0 or cols == 0:
        return image
    orig = image[sr][sc]
    if orig == new_color:
        return image
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != orig:
            return
        image[r][c] = new_color
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    dfs(sr, sc)
    return image

if __name__ == "__main__":
    img = [
        ['B','B','W'],
        ['W','W','W'],
        ['W','W','W'],
        ['B','B','B']
    ]
    out = flood_fill(img, 2, 2, 'G')
    print(out)
