local M = {}

function script_path()
  local str = debug.getinfo(2, "S").source:sub(2)
  return str:match("(.*/)")
end

local default_config = { storage_path = "~/.local/share/nvim/lazy/sandbox/ideas/" }
local framework_path = script_path() .. "../../framework/scripts/framework.py"

function M.setup(options)
  if options then
    M.options = options
  else
    M.options = default_config
  end
  vim.keymap.set('n', '<leader>gw', M.sandbox)
  vim.keymap.set('n', '<leader>ge', M.errors)
  vim.keymap.set('n', '<leader>gl', M.load)
  vim.keymap.set('n', '<leader>gm', string.format("<cmd>edit %s/../../main.*<CR>", script_path()))
  vim.keymap.set('n', '<leader>gc', "<cmd>cclose<CR><cmd>ToggleTerm<CR>")
end

function M.format()
  vim.cmd("%!clang-format")
end

function M.execute(cmd)
  vim.cmd(string.format("2TermExec direction=vertical display_name=exe size=80 cmd='%s'", cmd)) 
end

function M.errors()
  vim.cmd("cfile output")
  vim.cmd("copen")
end

function M.run()
  M.execute("./a.out")
  M.execute("rm ./a.out 2> /dev/null")
end

function M.sandbox ()
  M.format()
  vim.cmd("w")
  M.execute("g++ % 2>&1 | tee output")
  M.run()
end

function M.reset (opts)
  M.execute(string.format("python3 %s --reset --lang %s --storage %s", framework_path , opts, M.options.storage_path))
end

function M.save(opts)
  M.execute(string.format("python3 %s --save --storage %s", framework_path, M.options.storage_path))
end

function M.load(opts)
  require('telescope.builtin').find_files({cwd = M.options.storage_path})
end

return M
