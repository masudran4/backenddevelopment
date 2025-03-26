export function Menu(){
    return (
      <div className="navbar bg-base-100 shadow-sm mb-2">
        <div className="flex-1">
          <a className="btn btn-ghost text-xl">TodoApp</a>
        </div>
        <div className="flex-none">
        <ul className="menu menu-vertical lg:menu-horizontal rounded-box flex-auto">
                <li><a>Contact Us</a></li>
                <li><a>Services</a></li>
                <li><a>Login</a></li>
              </ul>
        </div>
    </div>
    )
}