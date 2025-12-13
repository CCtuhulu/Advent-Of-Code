# Advent of Code 2025 - Day 10: Factory
# Bruteforce solution using bitmasks (GF(2))

# Convert diagram like ".##." to bitmask
def diagram_to_mask(str)
  mask = 0
  str.each_char do |c|
    mask = (mask << 1) | (c == '#' ? 1 : 0)
  end
  mask
end

# Convert button indices like [0,3,4] to bitmask
def button_to_mask(indices, n)
  mask = 0
  indices.each do |i|
    mask |= 1 << (n - 1 - i)
  end
  mask
end

# Find minimum number of presses for one machine
def min_presses(target, buttons)
  m = buttons.length
  best = Float::INFINITY

  (0...(1 << m)).each do |combo|
    state = 0
    presses = 0

    m.times do |i|
      if ((combo >> i) & 1) == 1
        state ^= buttons[i]
        presses += 1
        break if presses >= best
      end
    end

    best = presses if state == target
  end

  best
end

total = 0

ARGF.each_line do |line|
  line.strip!
  next if line.empty?

  # Extract diagram
  diagram = line[/\[(.*?)\]/, 1]
  n = diagram.length
  target = diagram_to_mask(diagram)

  # Extract buttons
  button_strings = line.scan(/\((.*?)\)/)
  buttons = button_strings.map do |b|
    indices = b[0].split(",").map(&:to_i)
    button_to_mask(indices, n)
  end

  total += min_presses(target, buttons)
end

puts total
