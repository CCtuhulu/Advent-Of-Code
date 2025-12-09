lines = File.readlines("input.txt", chomp: true)

divider_index = lines.index("")

range_lines = lines[0...divider_index]

ranges = range_lines.map do |line|
  min, max = line.split("-").map(&:to_i)
  [min, max]
end

ranges.sort_by! { |min, _max| min }

merged_ranges = []

ranges.each do |min, max|
  if merged_ranges.empty? || min > merged_ranges.last[1] + 1
    merged_ranges << [min, max]
  else
    merged_ranges.last[1] = [merged_ranges.last[1], max].max
  end
end

total_fresh = merged_ranges.sum { |min, max| max - min + 1 }

puts total_fresh