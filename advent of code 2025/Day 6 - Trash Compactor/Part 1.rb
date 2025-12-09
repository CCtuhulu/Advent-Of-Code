lines = File.readlines("input.txt",chomp:true)

matrice = []

matrice = lines.map do |line|
    line.split
end

result = 0

(0...matrice[0].size).each do |i|
    j = matrice[0][i].to_i
    k = matrice[1][i].to_i
    l = matrice[2][i].to_i
    h = matrice[3][i].to_i
    m = matrice[4][i]

    if m == "+"
        result += j + k + l + h
    else
        result += (j*k*l*h)
    end
end

puts result
