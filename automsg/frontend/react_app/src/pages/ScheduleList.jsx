import { IoMenu, IoSearchSharp } from "react-icons/io5";
import { MdArrowDropDown } from "react-icons/md";
import { BsThreeDotsVertical } from "react-icons/bs";
import { Tab, Tabs } from "react-bootstrap";
import MessageCard from "../components/ui/MessageCard";

const ScheduleList = () => {
  return (
    <div className="container d-flex flex-column align-items-center justify-content-center ">
      <div className="Container d-flex w-75 justify-content-center p-5 mb-0">
          <div className="d-flex p-3 bg-secondary text-white w-100 justify-content-around align-self-center">
              <div className="d-flex bg-secondary text-white justify-content-around align-items-center w-50">
                  <IoMenu className=" me-3 fs-3"/>
                  <h3 className="me-5">Scheduler</h3>
                  <MdArrowDropDown className="fs-2"/>
              </div>
              <div className="d-flex bg-secondary text-white justify-content-center w-25">

                <IoSearchSharp className="me-5 fs-3"/>
                <BsThreeDotsVertical className="fs-3"/>
              </div>
          </div>
          
      </div>
      <div className="w-75 m-0 px-5">
        <Tabs className="d-flex justify-content-around">
          <Tab eventKey="home" title="Pending">
            <MessageCard />
            <MessageCard />
            <MessageCard />
          </Tab>
          <Tab eventKey="profile" title="Completed">
            Tab content for Profile
          </Tab>
          <Tab eventKey="failed" title="Failed">
            Tab content for Failed
          </Tab>
        </Tabs>
        {/* <button type="button" className="btn btn-primary position-relative">
          Pending <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-secondary">+99 <span className="visually-hidden">unread messages</span></span>
        </button>

        <button type="button" className="btn btn-primary position-relative">
          Completed <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-secondary">+99 <span className="visually-hidden">unread messages</span></span>
        </button>

        <button type="button" className="btn btn-primary position-relative">
          Failed <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-secondary">+99 <span className="visually-hidden">unread messages</span></span>
        </button> */}
      </div>
    </div>
  )
}

export default ScheduleList