lines = File.readlines("input.txt",chomp: true)

result = 0

lines.each do |i|
  array = i.chars.map(&:to_i)
  fst = array[0..-2].max()
  scd = array[array.index(fst)+1..].max()
  result += (fst.to_s + scd.to_s).to_i
end

puts result