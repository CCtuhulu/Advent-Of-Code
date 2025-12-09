lines = File.readlines("input.txt",chomp: true)

result = 0
(0..(lines.length-1)).each do |i|
    (0..(lines[i].length-1)).each do |j|
      neighbours = 0
      neighbours += 1 if i > 0 && lines[i-1][j] == '@'
      neighbours += 1 if i < lines.length-1 && lines[i+1][j] == '@'
      neighbours += 1 if i > 0 && j > 0 && lines[i-1][j-1] == '@'
      neighbours += 1 if j > 0 && lines[i][j-1] == '@'
      neighbours += 1 if i < lines.length-1 && j > 0 && lines[i+1][j-1] == '@'
      neighbours += 1 if i > 0 && j < lines[i].length-1 && lines[i-1][j+1] == '@'
      neighbours += 1 if j < lines[i].length-1 && lines[i][j+1] == '@'
      neighbours += 1 if i < lines.length-1 && j < lines[i].length-1 && lines[i+1][j+1] == '@'

      if neighbours < 4 and lines[i][j]=="@"
        result +=1
      end
    end
end

puts result