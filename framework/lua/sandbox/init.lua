function format()
  vim.cmd("%!clang-format")
end


function execute(cmd)
  vim.cmd(string.format("2TermExec direction=vertical display_name=exe size=80 cmd='%s'", cmd)) 
end


function errors()
  vim.cmd("cfile output")
  vim.cmd("copen")
end

function run()
  execute("./a.out")
  execute("rm ./a.out 2> /dev/null")
end

function sandbox ()
  format()
  vim.cmd("w")
  execute("g++ % 2>&1 | tee output")
  run()
end

function __sandbox_reset (opts)
  execute(string.format("python3 framework/scripts/framework.py --reset --lang %s", opts))
end

function __sandbox_save(opts)
  execute("python3 framework/scripts/framework.py --save")
end

vim.keymap.set('n', '<leader>gw', sandbox)
vim.keymap.set('n', '<leader>ge', errors)
vim.keymap.set('n', '<leader>gc', "<cmd>cclose<CR><cmd>ToggleTerm<CR>")

vim.api.nvim_create_user_command(
  "SReset",
  function(opts)
    __sandbox_reset(opts.args)
  end,
  { nargs = '?' }
)

vim.api.nvim_create_user_command(
  "SSave",
  function(opts)
    __sandbox_save(opts.args)
  end,
  { nargs = '?' }
)
