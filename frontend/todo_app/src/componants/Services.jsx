import { useState } from "react";
export function Services(){
    const [activeService,updateService] = useState(null);

    let service = ["Web Scraping","Api Testing","Functional Testing","Data Scraping"];
    return (
    service.map((item)=> <button role="tab" className={`tab btn btn-outline m-1 ${activeService==item?'tab-active':''}`} id={item} onClick={()=>updateService(item)}>{item}</button>)
    )
}