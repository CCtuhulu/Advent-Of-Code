lines = File.readlines("input.txt",chomp: true)

result = 0

lines.each do |i|
  array = i.chars.map(&:to_i)

  nmb = []
  index = 0
  12.downto(1) do |j|
    n = array[index..-j].max()
    slice = array[index..].index(n)
    index += slice + 1
    puts "#{n} #{index}"
    nmb << n.to_s
  end
  fnl = nmb.join
  puts fnl
  result += fnl.to_i
end

puts result