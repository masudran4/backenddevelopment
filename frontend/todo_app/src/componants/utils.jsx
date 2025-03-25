
export function AddPerson(prop){
    return (
        <div>
            <h1 className="text-green-500">{prop.name}</h1>
            {prop.children}
        </div>
        
    );
}