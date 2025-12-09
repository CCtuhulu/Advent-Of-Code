lines = File.readlines("input.txt", chomp: true)
height = lines.length
width  = lines[0].length

timelines = Array.new(height) { Array.new(width, 0) }

start_col = lines[0].index("S")
timelines[0][start_col] = 1 

(0...(height - 1)).each do |row|
  (0...width).each do |col|
    count = timelines[row][col]
    next if count == 0 

    cell_below = lines[row + 1][col]

    if cell_below == "."
      timelines[row + 1][col] += count
    elsif cell_below == "^"
      timelines[row + 1][col - 1] += count if col > 0
      timelines[row + 1][col + 1] += count if col < width - 1
    end
  end
end

total_timelines = timelines[height - 1].sum
puts total_timelines
